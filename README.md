# Distributed tracing + circuit breaker library

Shared by sibling microservices (`inventory`, `orders`).

## Install

```bash
python3.12 -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
pytest tests/ -q
```

## Circuit breaker

```python
from distributed_tracing import CircuitBreaker, CircuitOpenError

cb = CircuitBreaker("inventory", failure_threshold=5, recovery_timeout=30)
try:
    cb.call(lambda: client.get("/stock/sku-1"))
except CircuitOpenError:
    ...  # fail fast
```

## Tracing (OTLP → local Alloy :4318)

```bash
export OTEL_SERVICE_NAME=orders
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

```python
from distributed_tracing import configure_tracing, get_tracer, inject_context

configure_tracing()
tracer = get_tracer(__name__)
```

## Local-first

```bash
cd ../platform-ops
make local-gate REPO=distributed-tracing
make auto REPO=distributed-tracing TITLE="…"
```
