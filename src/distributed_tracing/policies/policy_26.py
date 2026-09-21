"""Resilience policy module 26 — tunable breaker + retry presets."""

from __future__ import annotations

from dataclasses import dataclass

from distributed_tracing.circuit_breaker import CircuitBreaker
from distributed_tracing.retry_policy import RetryPolicy


@dataclass(frozen=True)
class Policy26:
    name: str = "policy_26"
    failure_threshold: int = 4
    recovery_timeout: float = 36.0
    max_attempts: int = 4

    def breaker(self) -> CircuitBreaker:
        return CircuitBreaker(
            failure_threshold=self.failure_threshold,
            recovery_timeout=self.recovery_timeout,
            name=self.name,
        )

    def retry(self) -> RetryPolicy:
        return RetryPolicy(
            max_attempts=self.max_attempts,
            base_delay=0.01 * 26,
        )

    def describe(self) -> dict:
        return {
            "name": self.name,
            "failure_threshold": self.failure_threshold,
            "recovery_timeout": self.recovery_timeout,
            "max_attempts": self.max_attempts,
            "index": 26,
        }


DEFAULT_POLICY_26 = Policy26()
