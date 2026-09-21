from distributed_tracing.policies.policy_06 import DEFAULT_POLICY_06


def test_policy_06_describe():
    d = DEFAULT_POLICY_06.describe()
    assert d["index"] == 6
    assert DEFAULT_POLICY_06.breaker().name == "policy_06"


def test_policy_06_retry():
    r = DEFAULT_POLICY_06.retry()
    assert r.max_attempts >= 2
