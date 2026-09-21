# distributed-tracing library API

OSS OpenTelemetry helpers + circuit breaker. Documented from `__all__` and any HTTP routes found in code.

## Public exports

| Symbol | Notes |
|--------|-------|
| `CircuitBreaker` | exported from `distributed_tracing` |
| `CircuitOpenError` | exported from `distributed_tracing` |
| `CircuitState` | exported from `distributed_tracing` |
| `BreakerStats` | exported from `distributed_tracing` |
| `configure_tracing` | exported from `distributed_tracing` |
| `get_tracer` | exported from `distributed_tracing` |
| `inject_context` | exported from `distributed_tracing` |
| `extract_context` | exported from `distributed_tracing` |
| `start_span` | exported from `distributed_tracing` |
| `record_exception` | exported from `distributed_tracing` |
| `shutdown_tracing` | exported from `distributed_tracing` |
| `force_flush` | exported from `distributed_tracing` |
| `instrument_fastapi` | exported from `distributed_tracing` |
| `instrument_flask` | exported from `distributed_tracing` |
| `configure_metrics` | exported from `distributed_tracing` |
| `get_meter` | exported from `distributed_tracing` |
| `configure_logging_otel` | exported from `distributed_tracing` |
| `set_baggage` | exported from `distributed_tracing` |
| `get_baggage` | exported from `distributed_tracing` |
| `telemetry_status` | exported from `distributed_tracing` |

## HTTP

No FastAPI/Flask route decorators found — this package is a **library**, not a service.
