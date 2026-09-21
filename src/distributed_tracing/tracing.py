"""OpenTelemetry tracer bootstrap — OTLP HTTP/gRPC to Collector/Alloy/Jaeger."""

from __future__ import annotations

import logging
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
from opentelemetry.sdk.trace.sampling import (
    ALWAYS_ON,
    ParentBased,
    TraceIdRatioBased,
)
from opentelemetry.trace import Span, Status, StatusCode, Tracer
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

logger = logging.getLogger(__name__)
_propagator = TraceContextTextMapPropagator()
_configured = False
_provider: TracerProvider | None = None


def _sampler():
    ratio = float(os.getenv("OTEL_TRACES_SAMPLER_ARG", "1.0"))
    if ratio >= 1.0:
        return ParentBased(ALWAYS_ON)
    return ParentBased(TraceIdRatioBased(max(0.0, min(1.0, ratio))))


def configure_tracing(
    service_name: str | None = None,
    *,
    endpoint: str | None = None,
    console: bool | None = None,
    protocol: str | None = None,
) -> TracerProvider:
    """Idempotent tracer provider using OpenTelemetry OSS exporters."""
    global _configured, _provider
    if _configured and _provider is not None:
        return _provider

    name = service_name or os.getenv("OTEL_SERVICE_NAME", "app")
    ep = endpoint if endpoint is not None else os.getenv(
        "OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318"
    )
    use_console = (
        console
        if console is not None
        else os.getenv("OTEL_CONSOLE_EXPORTER", "false").lower()
        in {"1", "true", "yes"}
    )
    proto = (protocol or os.getenv("OTEL_EXPORTER_OTLP_PROTOCOL", "http/protobuf")).lower()

    resource = Resource.create(
        {
            "service.name": name,
            "service.version": os.getenv("SERVICE_VERSION", "0.2.0"),
            "deployment.environment": os.getenv("APP_ENV", "local"),
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
        }
    )
    provider = TracerProvider(resource=resource, sampler=_sampler())

    if ep:
        traces_url = f"{ep.rstrip('/')}/v1/traces"
        if proto.startswith("grpc"):
            try:
                from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
                    OTLPSpanExporter as GrpcExporter,
                )

                exporter: Any = GrpcExporter(
                    endpoint=ep.replace("http://", "").replace("https://", ""),
                    insecure=ep.startswith("http://"),
                )
            except Exception:  # pragma: no cover
                exporter = OTLPSpanExporter(endpoint=traces_url)
        else:
            exporter = OTLPSpanExporter(endpoint=traces_url)
        provider.add_span_processor(
            BatchSpanProcessor(
                exporter,
                max_queue_size=int(os.getenv("OTEL_BSP_MAX_QUEUE_SIZE", "2048")),
                schedule_delay_millis=int(
                    os.getenv("OTEL_BSP_SCHEDULE_DELAY", "2000")
                ),
                max_export_batch_size=int(
                    os.getenv("OTEL_BSP_MAX_EXPORT_BATCH_SIZE", "512")
                ),
            )
        )
    if use_console or not ep:
        provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))

    trace.set_tracer_provider(provider)
    _provider = provider
    _configured = True
    logger.info("tracing configured service=%s endpoint=%s", name, ep)
    return provider


def get_tracer(name: str = __name__) -> Tracer:
    if not _configured:
        configure_tracing()
    return trace.get_tracer(name)


def inject_context(carrier: dict[str, str]) -> dict[str, str]:
    _propagator.inject(carrier)
    return carrier


def extract_context(carrier: dict[str, str]) -> Any:
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


def force_flush(timeout_millis: int = 5000) -> bool:
    if _provider is None:
        return False
    return bool(_provider.force_flush(timeout_millis))


def shutdown_tracing() -> None:
    global _configured, _provider
    if _provider is not None:
        _provider.shutdown()
    _configured = False
    _provider = None
