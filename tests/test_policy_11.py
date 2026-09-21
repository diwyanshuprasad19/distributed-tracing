from distributed_tracing.policies.policy_11 import DEFAULT_POLICY_11


def test_policy_11_describe():
    d = DEFAULT_POLICY_11.describe()
    assert d["index"] == 11
    assert DEFAULT_POLICY_11.breaker().name == "policy_11"


def test_policy_11_retry():
    r = DEFAULT_POLICY_11.retry()
    assert r.max_attempts >= 2
