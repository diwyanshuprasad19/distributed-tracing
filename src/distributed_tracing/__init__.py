"""Production distributed tracing + resilience primitives (OpenTelemetry OSS)."""

from distributed_tracing.baggage_util import get_baggage, set_baggage
from distributed_tracing.circuit_breaker import (
    BreakerStats,
    CircuitBreaker,
    CircuitOpenError,
    CircuitState,
)
from distributed_tracing.fastapi_otel import instrument_fastapi
from distributed_tracing.flask_otel import instrument_flask
from distributed_tracing.health_telemetry import telemetry_status
from distributed_tracing.logging_otel import configure_logging_otel
from distributed_tracing.metrics import configure_metrics, get_meter
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

__all__ = [
    "CircuitBreaker",
    "CircuitOpenError",
    "CircuitState",
    "BreakerStats",
    "configure_tracing",
    "get_tracer",
    "inject_context",
    "extract_context",
    "start_span",
    "record_exception",
    "shutdown_tracing",
    "force_flush",
    "instrument_fastapi",
    "instrument_flask",
    "configure_metrics",
    "get_meter",
    "configure_logging_otel",
    "set_baggage",
    "get_baggage",
    "telemetry_status",
]
__version__ = "0.2.0"
