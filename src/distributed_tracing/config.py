"""Environment-driven configuration for the tracing library."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class TracingConfig:
    service_name: str
    endpoint: str
    console: bool
    protocol: str
    sample_ratio: float
    app_env: str

    @classmethod
    def from_env(cls, service_name: str | None = None) -> TracingConfig:
        return cls(
            service_name=service_name or os.getenv("OTEL_SERVICE_NAME", "app"),
            endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318"),
            console=os.getenv("OTEL_CONSOLE_EXPORTER", "false").lower() in {"1", "true", "yes"},
            protocol=os.getenv("OTEL_EXPORTER_OTLP_PROTOCOL", "http/protobuf"),
            sample_ratio=float(os.getenv("OTEL_TRACES_SAMPLER_ARG", "1.0")),
            app_env=os.getenv("APP_ENV", "local"),
        )
