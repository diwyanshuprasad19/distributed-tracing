"""Thread-safe circuit breaker (closed → open → half-open) for outbound calls."""

from __future__ import annotations

import threading
import time
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar

T = TypeVar("T")


class CircuitState(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitOpenError(RuntimeError):
    def __init__(self, retry_after: float) -> None:
        self.retry_after = retry_after
        super().__init__(f"circuit open; retry after {retry_after:.2f}s")


@dataclass
class BreakerStats:
    state: CircuitState
    failures: int
    successes: int
    opened_at: float | None
    last_failure_at: float | None
    half_open_trials: int


class CircuitBreaker(Generic[T]):
    """Protects a callable. Opens after ``failure_threshold`` consecutive failures."""

    def __init__(
        self,
        *,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        half_open_max_calls: int = 1,
        name: str = "default",
    ) -> None:
        if failure_threshold < 1:
            raise ValueError("failure_threshold must be >= 1")
        if recovery_timeout <= 0:
            raise ValueError("recovery_timeout must be > 0")
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls
        self.name = name
        self._state = CircuitState.CLOSED
        self._failures = 0
        self._successes = 0
        self._opened_at: float | None = None
        self._last_failure_at: float | None = None
        self._half_open_trials = 0
        self._lock = threading.RLock()

    def stats(self) -> BreakerStats:
        with self._lock:
            return BreakerStats(
                state=self._state,
                failures=self._failures,
                successes=self._successes,
                opened_at=self._opened_at,
                last_failure_at=self._last_failure_at,
                half_open_trials=self._half_open_trials,
            )

    def reset(self) -> None:
        with self._lock:
            self._state = CircuitState.CLOSED
            self._failures = 0
            self._successes = 0
            self._opened_at = None
            self._half_open_trials = 0

    def _transition_to_open(self) -> None:
        self._state = CircuitState.OPEN
        self._opened_at = time.monotonic()
        self._half_open_trials = 0

    def _maybe_half_open(self) -> None:
        if self._state != CircuitState.OPEN or self._opened_at is None:
            return
        if time.monotonic() - self._opened_at >= self.recovery_timeout:
            self._state = CircuitState.HALF_OPEN
            self._half_open_trials = 0

    def call(self, fn: Callable[[], T]) -> T:
        with self._lock:
            self._maybe_half_open()
            if self._state == CircuitState.OPEN:
                remaining = self.recovery_timeout - (
                    time.monotonic() - (self._opened_at or time.monotonic())
                )
                raise CircuitOpenError(max(0.0, remaining))
            if self._state == CircuitState.HALF_OPEN:
                if self._half_open_trials >= self.half_open_max_calls:
                    raise CircuitOpenError(self.recovery_timeout)
                self._half_open_trials += 1
        try:
            result = fn()
        except Exception:
            with self._lock:
                self._failures += 1
                self._last_failure_at = time.monotonic()
                if self._state == CircuitState.HALF_OPEN:
                    self._transition_to_open()
                elif self._failures >= self.failure_threshold:
                    self._transition_to_open()
            raise
        with self._lock:
            self._successes += 1
            self._failures = 0
            if self._state == CircuitState.HALF_OPEN:
                self._state = CircuitState.CLOSED
                self._opened_at = None
                self._half_open_trials = 0
        return result
