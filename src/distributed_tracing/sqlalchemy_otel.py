"""Instrument SQLAlchemy engines for DB spans."""

from __future__ import annotations

from typing import Any


def instrument_sqlalchemy(engine: Any | None = None) -> None:
    try:
        from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

        if engine is not None:
            SQLAlchemyInstrumentor().instrument(engine=engine)
        else:
            SQLAlchemyInstrumentor().instrument()
    except Exception:  # pragma: no cover
        pass
