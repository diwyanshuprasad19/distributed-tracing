"""Instrument FastAPI with OpenTelemetry contrib (OSS)."""

from __future__ import annotations

import os
from typing import Any

from distributed_tracing.tracing import configure_tracing


def instrument_fastapi(app: Any, *, service_name: str | None = None) -> Any:
    configure_tracing(service_name or os.getenv("OTEL_SERVICE_NAME", "fastapi-app"))
    try:
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

        FastAPIInstrumentor.instrument_app(
            app,
            excluded_urls=os.getenv(
                "OTEL_PYTHON_FASTAPI_EXCLUDED_URLS",
                "health,ready,metrics,docs,openapi.json,redoc",
            ),
        )
    except Exception:  # pragma: no cover
        pass
    return app
