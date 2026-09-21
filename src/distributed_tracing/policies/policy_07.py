"""Resilience policy module 07 — tunable breaker + retry presets."""

from __future__ import annotations

from dataclasses import dataclass

from distributed_tracing.circuit_breaker import CircuitBreaker
from distributed_tracing.retry_policy import RetryPolicy


@dataclass(frozen=True)
class Policy07:
    name: str = "policy_07"
    failure_threshold: int = 5
    recovery_timeout: float = 17.0
    max_attempts: int = 5

    def breaker(self) -> CircuitBreaker:
        return CircuitBreaker(
            failure_threshold=self.failure_threshold,
            recovery_timeout=self.recovery_timeout,
            name=self.name,
        )

    def retry(self) -> RetryPolicy:
        return RetryPolicy(
            max_attempts=self.max_attempts,
            base_delay=0.01 * 7,
        )

    def describe(self) -> dict:
        return {
            "name": self.name,
            "failure_threshold": self.failure_threshold,
            "recovery_timeout": self.recovery_timeout,
            "max_attempts": self.max_attempts,
            "index": 7,
        }


DEFAULT_POLICY_07 = Policy07()
