"""Instrument httpx clients for outbound distributed traces."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def instrument_httpx() -> None:
    try:
        from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor

        HTTPXClientInstrumentor().instrument()
    except Exception as exc:  # pragma: no cover
        logger.warning("httpx otel instrument failed: %s", exc)
