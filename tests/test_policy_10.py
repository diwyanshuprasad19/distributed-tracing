from distributed_tracing.policies.policy_10 import DEFAULT_POLICY_10


def test_policy_10_describe():
    d = DEFAULT_POLICY_10.describe()
    assert d["index"] == 10
    assert DEFAULT_POLICY_10.breaker().name == "policy_10"


def test_policy_10_retry():
    r = DEFAULT_POLICY_10.retry()
    assert r.max_attempts >= 2
