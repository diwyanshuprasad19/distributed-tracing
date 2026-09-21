from distributed_tracing.policies.policy_03 import DEFAULT_POLICY_03


def test_policy_03_describe():
    d = DEFAULT_POLICY_03.describe()
    assert d["index"] == 3
    assert DEFAULT_POLICY_03.breaker().name == "policy_03"


def test_policy_03_retry():
    r = DEFAULT_POLICY_03.retry()
    assert r.max_attempts >= 2
