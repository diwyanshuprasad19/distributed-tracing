from distributed_tracing.policies.policy_01 import DEFAULT_POLICY_01
from distributed_tracing.policies.policy_10 import DEFAULT_POLICY_10
from distributed_tracing.retry_policy import RetryPolicy
from distributed_tracing.config import TracingConfig
from distributed_tracing.health_telemetry import telemetry_status
from distributed_tracing.catalogs.attrs_01 import keys_01


def test_policies():
    assert DEFAULT_POLICY_01.breaker().name == "policy_01"
    assert DEFAULT_POLICY_10.describe()["index"] == 10


def test_retry_success():
    n = {"c": 0}

    def flaky():
        n["c"] += 1
        if n["c"] < 2:
            raise ConnectionError("tmp")
        return "ok"

    assert RetryPolicy(max_attempts=3, base_delay=0.001).run(flaky) == "ok"


def test_config_and_status():
    cfg = TracingConfig.from_env("unit")
    assert cfg.service_name == "unit"
    st = telemetry_status()
    assert "otlp_endpoint" in st
    assert len(keys_01()) == 20
