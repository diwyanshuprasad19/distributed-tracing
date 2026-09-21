"""Resilience policy module 22 — tunable breaker + retry presets."""

from __future__ import annotations

from dataclasses import dataclass

from distributed_tracing.circuit_breaker import CircuitBreaker
from distributed_tracing.retry_policy import RetryPolicy


@dataclass(frozen=True)
class Policy22:
    name: str = "policy_22"
    failure_threshold: int = 5
    recovery_timeout: float = 32.0
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
            base_delay=0.01 * 22,
        )

    def describe(self) -> dict:
        return {
            "name": self.name,
            "failure_threshold": self.failure_threshold,
            "recovery_timeout": self.recovery_timeout,
            "max_attempts": self.max_attempts,
            "index": 22,
        }


DEFAULT_POLICY_22 = Policy22()
