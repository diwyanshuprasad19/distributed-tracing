from distributed_tracing.policies.policy_01 import DEFAULT_POLICY_01


def test_policy_01_describe():
    d = DEFAULT_POLICY_01.describe()
    assert d["index"] == 1
    assert DEFAULT_POLICY_01.breaker().name == "policy_01"


def test_policy_01_retry():
    r = DEFAULT_POLICY_01.retry()
    assert r.max_attempts >= 2
