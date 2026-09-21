"""distributed-tracing — OTel + circuit breaker for sibling microservices."""

from distributed_tracing.circuit_breaker import (
    CircuitBreaker,
    CircuitOpenError,
    CircuitState,
    CircuitStats,
)
from distributed_tracing.tracing import (
    configure_tracing,
    extract_context,
    get_tracer,
    inject_context,
    record_exception,
    start_span,
)

__all__ = [
    "CircuitBreaker",
    "CircuitOpenError",
    "CircuitState",
    "CircuitStats",
    "configure_tracing",
    "extract_context",
    "get_tracer",
    "inject_context",
    "record_exception",
    "start_span",
]
