"""Resilience policy module 10 — tunable breaker + retry presets."""

from __future__ import annotations

from dataclasses import dataclass

from distributed_tracing.circuit_breaker import CircuitBreaker
from distributed_tracing.retry_policy import RetryPolicy


@dataclass(frozen=True)
class Policy10:
    name: str = "policy_10"
    failure_threshold: int = 3
    recovery_timeout: float = 20.0
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
            base_delay=0.01 * 10,
        )

    def describe(self) -> dict:
        return {
            "name": self.name,
            "failure_threshold": self.failure_threshold,
            "recovery_timeout": self.recovery_timeout,
            "max_attempts": self.max_attempts,
            "index": 10,
        }


DEFAULT_POLICY_10 = Policy10()
