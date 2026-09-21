"""OpenTelemetry metrics (OTLP) — request counters and latency histograms."""

from __future__ import annotations

import os
from typing import Any

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource

_configured = False
_meter_provider: MeterProvider | None = None


def configure_metrics(service_name: str | None = None) -> MeterProvider:
    global _configured, _meter_provider
    if _configured and _meter_provider is not None:
        return _meter_provider
    name = service_name or os.getenv("OTEL_SERVICE_NAME", "app")
    resource = Resource.create({"service.name": name})
    ep = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318")
    readers: list[Any] = []
    try:
        from opentelemetry.exporter.otlp.proto.http.metric_exporter import (
            OTLPMetricExporter,
        )
        from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

        exporter = OTLPMetricExporter(endpoint=f"{ep.rstrip('/')}/v1/metrics")
        readers.append(PeriodicExportingMetricReader(exporter, export_interval_millis=5000))
    except Exception:  # pragma: no cover
        pass
    provider = MeterProvider(resource=resource, metric_readers=readers)
    metrics.set_meter_provider(provider)
    _meter_provider = provider
    _configured = True
    return provider


def get_meter(name: str = __name__):
    if not _configured:
        configure_metrics()
    return metrics.get_meter(name)
