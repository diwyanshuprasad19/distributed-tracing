"""Instrument SQLAlchemy engines for DB spans."""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger(__name__)


def instrument_sqlalchemy(engine: Any | None = None) -> None:
    try:
        from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

        if engine is not None:
            SQLAlchemyInstrumentor().instrument(engine=engine)
        else:
            SQLAlchemyInstrumentor().instrument()
    except Exception as exc:  # pragma: no cover
        logger.warning("sqlalchemy otel instrument failed: %s", exc)
