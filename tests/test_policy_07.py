from distributed_tracing.policies.policy_07 import DEFAULT_POLICY_07


def test_policy_07_describe():
    d = DEFAULT_POLICY_07.describe()
    assert d["index"] == 7
    assert DEFAULT_POLICY_07.breaker().name == "policy_07"


def test_policy_07_retry():
    r = DEFAULT_POLICY_07.retry()
    assert r.max_attempts >= 2
