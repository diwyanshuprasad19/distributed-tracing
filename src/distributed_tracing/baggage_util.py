"""W3C baggage helpers for cross-service correlation."""

from __future__ import annotations

from opentelemetry import baggage, context


def set_baggage(key: str, value: str):
    ctx = baggage.set_baggage(key, value)
    return context.attach(ctx)


def get_baggage(key: str) -> str | None:
    return baggage.get_baggage(key)
