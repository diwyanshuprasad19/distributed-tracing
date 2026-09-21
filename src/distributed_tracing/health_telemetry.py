"""Report whether tracing/metrics providers are live."""

from __future__ import annotations

import os
from typing import Any

from opentelemetry import metrics, trace
from opentelemetry.sdk.trace import TracerProvider


def telemetry_status() -> dict[str, Any]:
    provider = trace.get_tracer_provider()
    meter_provider = metrics.get_meter_provider()
    return {
        "tracing_configured": isinstance(provider, TracerProvider),
        "provider": type(provider).__name__,
        "meter_provider": type(meter_provider).__name__,
        "otlp_endpoint": os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318"),
        "service_name": os.getenv("OTEL_SERVICE_NAME", ""),
        "sampler_arg": os.getenv("OTEL_TRACES_SAMPLER_ARG", "1.0"),
    }
