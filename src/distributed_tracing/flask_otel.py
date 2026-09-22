"""Instrument Flask with OpenTelemetry contrib (OSS)."""

from __future__ import annotations

import logging
import os
from typing import Any

from distributed_tracing.tracing import configure_tracing

logger = logging.getLogger(__name__)


def instrument_flask(app: Any, *, service_name: str | None = None) -> Any:
    configure_tracing(service_name or os.getenv("OTEL_SERVICE_NAME", "flask-app"))
    try:
        from opentelemetry.instrumentation.flask import FlaskInstrumentor

        FlaskInstrumentor().instrument_app(app)
    except Exception as exc:  # pragma: no cover
        logger.warning("flask otel instrument failed: %s", exc)
    return app
