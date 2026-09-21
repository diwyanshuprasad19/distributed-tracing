from distributed_tracing.policies.policy_05 import DEFAULT_POLICY_05


def test_policy_05_describe():
    d = DEFAULT_POLICY_05.describe()
    assert d["index"] == 5
    assert DEFAULT_POLICY_05.breaker().name == "policy_05"


def test_policy_05_retry():
    r = DEFAULT_POLICY_05.retry()
    assert r.max_attempts >= 2
