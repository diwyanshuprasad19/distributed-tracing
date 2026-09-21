from distributed_tracing.policies.policy_12 import DEFAULT_POLICY_12


def test_policy_12_describe():
    d = DEFAULT_POLICY_12.describe()
    assert d["index"] == 12
    assert DEFAULT_POLICY_12.breaker().name == "policy_12"


def test_policy_12_retry():
    r = DEFAULT_POLICY_12.retry()
    assert r.max_attempts >= 2
