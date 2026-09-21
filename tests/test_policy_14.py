from distributed_tracing.policies.policy_14 import DEFAULT_POLICY_14


def test_policy_14_describe():
    d = DEFAULT_POLICY_14.describe()
    assert d["index"] == 14
    assert DEFAULT_POLICY_14.breaker().name == "policy_14"


def test_policy_14_retry():
    r = DEFAULT_POLICY_14.retry()
    assert r.max_attempts >= 2
