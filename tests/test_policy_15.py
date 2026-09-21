from distributed_tracing.policies.policy_15 import DEFAULT_POLICY_15


def test_policy_15_describe():
    d = DEFAULT_POLICY_15.describe()
    assert d["index"] == 15
    assert DEFAULT_POLICY_15.breaker().name == "policy_15"


def test_policy_15_retry():
    r = DEFAULT_POLICY_15.retry()
    assert r.max_attempts >= 2
