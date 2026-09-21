"""Retry policy used with circuit breaker for transient failures."""

from __future__ import annotations

import random
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")


@dataclass
class RetryPolicy:
    max_attempts: int = 3
    base_delay: float = 0.05
    max_delay: float = 2.0
    jitter: bool = True
    retry_on: tuple[type[BaseException], ...] = (TimeoutError, ConnectionError)

    def run(self, fn: Callable[[], T]) -> T:
        last: BaseException | None = None
        for attempt in range(1, self.max_attempts + 1):
            try:
                return fn()
            except self.retry_on as exc:
                last = exc
                if attempt >= self.max_attempts:
                    break
                delay = min(self.max_delay, self.base_delay * (2 ** (attempt - 1)))
                if self.jitter:
                    delay *= 0.5 + random.random()
                time.sleep(delay)
        assert last is not None
        raise last
