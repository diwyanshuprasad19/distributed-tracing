"""OpenTelemetry setup for distributed microservices (OTLP → Alloy/local collector)."""

from __future__ import annotations

import os
from typing import Any

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.trace import Span, Status, StatusCode, Tracer
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

_propagator = TraceContextTextMapPropagator()
_configured = False


def configure_tracing(
    service_name: str | None = None,
    *,
    endpoint: str | None = None,
    console: bool | None = None,
) -> TracerProvider:
    """Idempotent tracer provider. Uses OTEL_* env when args omitted."""
    global _configured
    name = service_name or os.getenv("OTEL_SERVICE_NAME", "app")
    ep = endpoint if endpoint is not None else os.getenv(
        "OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318"
    )
    use_console = (
        console
        if console is not None
        else os.getenv("OTEL_CONSOLE_EXPORTER", "false").lower() in {"1", "true", "yes"}
    )

    resource = Resource.create(
        {
            "service.name": name,
            "deployment.environment": os.getenv("APP_ENV", "local"),
        }
    )
    provider = TracerProvider(resource=resource)
    if ep:
        # OTLP HTTP exporter expects base URL; SDK appends /v1/traces
        exporter = OTLPSpanExporter(endpoint=f"{ep.rstrip('/')}/v1/traces")
        provider.add_span_processor(BatchSpanProcessor(exporter))
    if use_console or not ep:
        provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
    trace.set_tracer_provider(provider)
    _configured = True
    return provider


def get_tracer(name: str = __name__) -> Tracer:
    if not _configured and not isinstance(trace.get_tracer_provider(), TracerProvider):
        configure_tracing()
    return trace.get_tracer(name)


def inject_context(carrier: dict[str, str]) -> dict[str, str]:
    """Inject W3C traceparent into outbound HTTP headers."""
    _propagator.inject(carrier)
    return carrier


def extract_context(carrier: dict[str, str]) -> Any:
    """Extract parent context from inbound HTTP headers."""
    return _propagator.extract(carrier)


def start_span(name: str, *, attributes: dict[str, Any] | None = None) -> Span:
    tracer = get_tracer("distributed_tracing")
    span = tracer.start_span(name)
    if attributes:
        for k, v in attributes.items():
            span.set_attribute(k, v)
    return span


def record_exception(span: Span, exc: BaseException) -> None:
    span.record_exception(exc)
    span.set_status(Status(StatusCode.ERROR, str(exc)))
