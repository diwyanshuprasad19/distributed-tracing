# distributed-tracing

Production OpenTelemetry library for Python microservices:

- OTLP HTTP/gRPC exporters → Alloy / Collector / Jaeger
- FastAPI / Flask / httpx / SQLAlchemy instrumentors (OSS contrib)
- Circuit breaker + retry policies
- W3C TraceContext + Baggage (+ optional B3)
- Metrics + logging correlation

```bash
pip install -e ".[dev]"
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
pytest -q
```
