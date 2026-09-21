from distributed_tracing.policies.policy_04 import DEFAULT_POLICY_04


def test_policy_04_describe():
    d = DEFAULT_POLICY_04.describe()
    assert d["index"] == 4
    assert DEFAULT_POLICY_04.breaker().name == "policy_04"


def test_policy_04_retry():
    r = DEFAULT_POLICY_04.retry()
    assert r.max_attempts >= 2
