"""Circuit breaker for downstream microservice calls (closed → open → half-open)."""

from __future__ import annotations

import threading
import time
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import TypeVar

T = TypeVar("T")


class CircuitState(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitOpenError(RuntimeError):
    """Raised when the breaker is open and calls are short-circuited."""

    def __init__(self, name: str, retry_after: float) -> None:
        self.name = name
        self.retry_after = retry_after
        super().__init__(f"circuit '{name}' is open; retry after {retry_after:.2f}s")


@dataclass
class CircuitStats:
    state: CircuitState
    failures: int
    successes: int
    opened_at: float | None


class CircuitBreaker:
    """Failure-threshold circuit breaker with half-open probe.

    Edge cases covered by tests:
    - success resets failure count in CLOSED
    - OPEN rejects until recovery_timeout
    - HALF_OPEN allows one probe; success → CLOSED, failure → OPEN
    - thread-safe under concurrent callers
    """

    def __init__(
        self,
        name: str,
        *,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        half_open_success_threshold: int = 1,
        clock: Callable[[], float] | None = None,
    ) -> None:
        if failure_threshold < 1:
            raise ValueError("failure_threshold must be >= 1")
        if recovery_timeout <= 0:
            raise ValueError("recovery_timeout must be > 0")
        if half_open_success_threshold < 1:
            raise ValueError("half_open_success_threshold must be >= 1")
        self.name = name
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_success_threshold = half_open_success_threshold
        self._clock = clock or time.monotonic
        self._lock = threading.RLock()
        self._state = CircuitState.CLOSED
        self._failures = 0
        self._successes = 0
        self._opened_at: float | None = None
        self._half_open_inflight = False

    def stats(self) -> CircuitStats:
        with self._lock:
            return CircuitStats(
                state=self._state,
                failures=self._failures,
                successes=self._successes,
                opened_at=self._opened_at,
            )

    def call(self, fn: Callable[[], T]) -> T:
        self._before_call()
        try:
            result = fn()
        except Exception:
            self._on_failure()
            raise
        self._on_success()
        return result

    def _before_call(self) -> None:
        with self._lock:
            now = self._clock()
            if self._state == CircuitState.OPEN:
                assert self._opened_at is not None
                elapsed = now - self._opened_at
                if elapsed < self.recovery_timeout:
                    raise CircuitOpenError(self.name, self.recovery_timeout - elapsed)
                self._state = CircuitState.HALF_OPEN
                self._successes = 0
                self._half_open_inflight = True
                return
            if self._state == CircuitState.HALF_OPEN and self._half_open_inflight:
                # Only one probe at a time
                raise CircuitOpenError(self.name, 0.05)
            if self._state == CircuitState.HALF_OPEN:
                self._half_open_inflight = True

    def _on_success(self) -> None:
        with self._lock:
            self._half_open_inflight = False
            if self._state == CircuitState.HALF_OPEN:
                self._successes += 1
                if self._successes >= self.half_open_success_threshold:
                    self._state = CircuitState.CLOSED
                    self._failures = 0
                    self._successes = 0
                    self._opened_at = None
                return
            self._failures = 0

    def _on_failure(self) -> None:
        with self._lock:
            self._half_open_inflight = False
            if self._state == CircuitState.HALF_OPEN:
                self._trip()
                return
            self._failures += 1
            if self._failures >= self.failure_threshold:
                self._trip()

    def _trip(self) -> None:
        self._state = CircuitState.OPEN
        self._opened_at = self._clock()
        self._successes = 0
