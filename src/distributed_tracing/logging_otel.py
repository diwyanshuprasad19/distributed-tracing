"""Bridge stdlib logging → OpenTelemetry (trace-correlated logs)."""

from __future__ import annotations

import logging
import os


def configure_logging_otel(level: int | None = None) -> None:
    lvl = (
        level
        if level is not None
        else getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO)
    )
    logging.basicConfig(
        level=lvl,
        format="%(asctime)s %(levelname)s [%(name)s] trace_id=%(otelTraceID)s span_id=%(otelSpanID)s %(message)s",
    )
    try:
        from opentelemetry.instrumentation.logging import LoggingInstrumentor

        LoggingInstrumentor().instrument(set_logging_format=True)
    except Exception:  # pragma: no cover
        pass
