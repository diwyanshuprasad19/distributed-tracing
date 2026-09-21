from distributed_tracing.policies.policy_13 import DEFAULT_POLICY_13


def test_policy_13_describe():
    d = DEFAULT_POLICY_13.describe()
    assert d["index"] == 13
    assert DEFAULT_POLICY_13.breaker().name == "policy_13"


def test_policy_13_retry():
    r = DEFAULT_POLICY_13.retry()
    assert r.max_attempts >= 2
