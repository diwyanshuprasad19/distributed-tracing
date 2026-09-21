"""Instrument Flask with OpenTelemetry contrib (OSS)."""

from __future__ import annotations

import os
from typing import Any

from distributed_tracing.tracing import configure_tracing


def instrument_flask(app: Any, *, service_name: str | None = None) -> Any:
    configure_tracing(service_name or os.getenv("OTEL_SERVICE_NAME", "flask-app"))
    try:
        from opentelemetry.instrumentation.flask import FlaskInstrumentor

        FlaskInstrumentor().instrument_app(app)
    except Exception:  # pragma: no cover
        pass
    return app
