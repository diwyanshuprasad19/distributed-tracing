"""ASGI/WSGI middleware helpers for request id + span attributes."""

from __future__ import annotations

import time
import uuid
from collections.abc import Callable
from typing import Any


def attach_request_id(headers: dict[str, str]) -> str:
    rid = headers.get("x-request-id") or headers.get("X-Request-Id") or str(uuid.uuid4())
    return rid


class TimingContext:
    def __init__(self) -> None:
        self.start = time.perf_counter()

    def elapsed_ms(self) -> float:
        return (time.perf_counter() - self.start) * 1000.0


def with_timing(fn: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        t = TimingContext()
        try:
            return fn(*args, **kwargs)
        finally:
            _ = t.elapsed_ms()

    return wrapper
