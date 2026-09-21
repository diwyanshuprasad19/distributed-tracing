"""Resilience policy module 04 — tunable breaker + retry presets."""

from __future__ import annotations

from dataclasses import dataclass

from distributed_tracing.circuit_breaker import CircuitBreaker
from distributed_tracing.retry_policy import RetryPolicy


@dataclass(frozen=True)
class Policy04:
    name: str = "policy_04"
    failure_threshold: int = 7
    recovery_timeout: float = 14.0
    max_attempts: int = 2

    def breaker(self) -> CircuitBreaker:
        return CircuitBreaker(
            failure_threshold=self.failure_threshold,
            recovery_timeout=self.recovery_timeout,
            name=self.name,
        )

    def retry(self) -> RetryPolicy:
        return RetryPolicy(
            max_attempts=self.max_attempts,
            base_delay=0.01 * 4,
        )

    def describe(self) -> dict:
        return {
            "name": self.name,
            "failure_threshold": self.failure_threshold,
            "recovery_timeout": self.recovery_timeout,
            "max_attempts": self.max_attempts,
            "index": 4,
        }


DEFAULT_POLICY_04 = Policy04()
