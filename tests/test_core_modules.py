"""CORE coverage for distributed_tracing helpers (non-catalog modules)."""

from __future__ import annotations

import logging
from unittest.mock import MagicMock

import pytest

from distributed_tracing import CircuitBreaker, CircuitOpenError, CircuitState
from distributed_tracing.baggage_util import get_baggage, set_baggage
from distributed_tracing.circuit_breaker import CircuitBreaker as CB
from distributed_tracing.errors import ConfigurationError, ExportError, TracingError
from distributed_tracing.fastapi_otel import instrument_fastapi
from distributed_tracing.flask_otel import instrument_flask
from distributed_tracing.httpx_otel import instrument_httpx
from distributed_tracing.logging_otel import configure_logging_otel
from distributed_tracing.metrics import configure_metrics, get_meter
from distributed_tracing.middleware import TimingContext, attach_request_id, with_timing
from distributed_tracing.propagators import configure_propagators
from distributed_tracing.retry_policy import RetryPolicy
from distributed_tracing.span_helpers import enrich, set_db_attrs, set_http_attrs, set_rpc_attrs
from distributed_tracing.sqlalchemy_otel import instrument_sqlalchemy
from distributed_tracing.tracing import (
    configure_tracing,
    extract_context,
    force_flush,
    get_tracer,
    inject_context,
    record_exception,
    shutdown_tracing,
    start_span,
)


def test_middleware_helpers():
    rid = attach_request_id({})
    assert isinstance(rid, str) and len(rid) > 0
    assert attach_request_id({"x-request-id": "abc"}) == "abc"
    assert attach_request_id({"X-Request-Id": "xyz"}) == "xyz"
    t = TimingContext()
    assert t.elapsed_ms() >= 0

    @with_timing
    def add(a, b):
        return a + b

    assert add(1, 2) == 3


def test_span_helpers():
    configure_tracing("span-helpers", endpoint="", console=True)
    span = MagicMock()
    set_http_attrs(span, method="GET", route="/x", status=200)
    set_db_attrs(span, system="sqlite", statement="SELECT 1", name="main")
    set_rpc_attrs(span, service="svc", method="Call")
    enrich(span, {"k": 1, "skip": None})
    assert span.set_attribute.call_count >= 7


def test_propagators_and_baggage(monkeypatch):
    configure_propagators(enable_b3=False)
    monkeypatch.setenv("OTEL_PROPAGATORS", "tracecontext,baggage,b3")
    configure_propagators(enable_b3=None)
    configure_propagators(enable_b3=True)
    token = set_baggage("tenant", "acme")
    assert get_baggage("tenant") == "acme"
    from opentelemetry import context

    context.detach(token)


def test_instrumentors_and_logging():
    instrument_httpx()
    instrument_sqlalchemy(None)
    instrument_sqlalchemy(MagicMock())
    configure_logging_otel(level=logging.WARNING)
    instrument_fastapi(MagicMock(), service_name="fastapi-cov")
    instrument_flask(MagicMock(), service_name="flask-cov")


def test_errors_taxonomy():
    assert issubclass(ConfigurationError, TracingError)
    assert issubclass(ExportError, TracingError)
    with pytest.raises(TracingError):
        raise ConfigurationError("bad")


def test_metrics_configure_idempotent(monkeypatch):
    import distributed_tracing.metrics as m

    m._configured = False
    m._meter_provider = None
    monkeypatch.setenv("OTEL_SERVICE_NAME", "metrics-cov")
    p1 = configure_metrics("metrics-cov")
    p2 = configure_metrics("metrics-cov")
    assert p1 is p2
    assert get_meter("m") is not None


def test_tracing_sampler_ratio_and_grpc(monkeypatch):
    shutdown_tracing()
    monkeypatch.setenv("OTEL_TRACES_SAMPLER_ARG", "0.5")
    p = configure_tracing(
        "ratio-svc", endpoint="http://localhost:4318", console=False, protocol="http"
    )
    assert p is not None
    shutdown_tracing()
    monkeypatch.setenv("OTEL_TRACES_SAMPLER_ARG", "1.0")
    configure_tracing("grpc-svc", endpoint="http://localhost:4317", console=True, protocol="grpc")
    carrier: dict[str, str] = {}
    inject_context(carrier)
    extract_context(carrier)
    span = start_span("work", attributes={"a": 1})
    try:
        raise RuntimeError("boom")
    except RuntimeError as exc:
        record_exception(span, exc)
    span.end()
    assert force_flush(100) in {True, False}
    get_tracer("x")
    shutdown_tracing()
    assert force_flush() is False


def test_circuit_half_open_success_and_validation():
    with pytest.raises(ValueError):
        CB(failure_threshold=0)
    with pytest.raises(ValueError):
        CB(recovery_timeout=0)
    b = CircuitBreaker(failure_threshold=1, recovery_timeout=0.01, half_open_max_calls=1)
    with pytest.raises(RuntimeError):
        b.call(lambda: (_ for _ in ()).throw(RuntimeError("fail")))
    assert b.stats().state == CircuitState.OPEN
    import time

    time.sleep(0.02)
    assert b.call(lambda: 42) == 42
    assert b.stats().state == CircuitState.CLOSED
    b.reset()
    with pytest.raises(RuntimeError):
        b.call(lambda: (_ for _ in ()).throw(RuntimeError("fail")))
    time.sleep(0.02)
    with pytest.raises(RuntimeError):
        b.call(lambda: (_ for _ in ()).throw(RuntimeError("fail-ho")))
    assert b.stats().state == CircuitState.OPEN
    time.sleep(0.02)
    b2 = CircuitBreaker(failure_threshold=1, recovery_timeout=0.01, half_open_max_calls=1)
    with pytest.raises(RuntimeError):
        b2.call(lambda: (_ for _ in ()).throw(RuntimeError("x")))
    time.sleep(0.02)
    with b2._lock:
        b2._maybe_half_open()
        b2._half_open_trials = b2.half_open_max_calls
    with pytest.raises(CircuitOpenError):
        b2.call(lambda: 1)


def test_retry_exhausts():
    with pytest.raises(ConnectionError):
        RetryPolicy(max_attempts=2, base_delay=0.001, jitter=False).run(
            lambda: (_ for _ in ()).throw(ConnectionError("nope"))
        )
