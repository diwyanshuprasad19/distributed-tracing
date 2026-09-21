"""Edge-case tests for circuit breaker + tracing helpers."""

from __future__ import annotations

import pytest

from distributed_tracing.circuit_breaker import CircuitBreaker, CircuitOpenError, CircuitState
from distributed_tracing.tracing import extract_context, inject_context


class FakeClock:
    def __init__(self) -> None:
        self.t = 0.0

    def __call__(self) -> float:
        return self.t

    def advance(self, dt: float) -> None:
        self.t += dt


def test_closed_opens_after_threshold() -> None:
    clock = FakeClock()
    cb = CircuitBreaker("inv", failure_threshold=3, recovery_timeout=10, clock=clock)

    def boom() -> None:
        raise TimeoutError("down")

    for _ in range(3):
        with pytest.raises(TimeoutError):
            cb.call(boom)
    assert cb.stats().state == CircuitState.OPEN
    with pytest.raises(CircuitOpenError):
        cb.call(lambda: "ok")


def test_open_recovers_to_half_open_then_closed() -> None:
    clock = FakeClock()
    cb = CircuitBreaker("inv", failure_threshold=2, recovery_timeout=5, clock=clock)
    for _ in range(2):
        with pytest.raises(RuntimeError):
            cb.call(lambda: (_ for _ in ()).throw(RuntimeError("x")))
    assert cb.stats().state == CircuitState.OPEN
    clock.advance(5.0)
    assert cb.call(lambda: 42) == 42
    assert cb.stats().state == CircuitState.CLOSED
    assert cb.stats().failures == 0


def test_half_open_failure_reopens() -> None:
    clock = FakeClock()
    cb = CircuitBreaker("inv", failure_threshold=1, recovery_timeout=2, clock=clock)
    with pytest.raises(ValueError):
        cb.call(lambda: (_ for _ in ()).throw(ValueError("e")))
    assert cb.stats().state == CircuitState.OPEN
    clock.advance(2.0)

    def boom() -> None:
        raise ConnectionError("still down")

    with pytest.raises(ConnectionError):
        cb.call(boom)
    assert cb.stats().state == CircuitState.OPEN


def test_success_resets_failure_count() -> None:
    clock = FakeClock()
    cb = CircuitBreaker("inv", failure_threshold=3, recovery_timeout=10, clock=clock)
    with pytest.raises(RuntimeError):
        cb.call(lambda: (_ for _ in ()).throw(RuntimeError("a")))
    with pytest.raises(RuntimeError):
        cb.call(lambda: (_ for _ in ()).throw(RuntimeError("b")))
    assert cb.call(lambda: "ok") == "ok"
    assert cb.stats().failures == 0
    assert cb.stats().state == CircuitState.CLOSED


def test_invalid_config() -> None:
    with pytest.raises(ValueError):
        CircuitBreaker("x", failure_threshold=0)
    with pytest.raises(ValueError):
        CircuitBreaker("x", recovery_timeout=0)


def test_trace_context_roundtrip() -> None:
    carrier: dict[str, str] = {}
    # Without an active span, inject may no-op; still must not crash
    inject_context(carrier)
    ctx = extract_context({"traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"})
    assert ctx is not None
