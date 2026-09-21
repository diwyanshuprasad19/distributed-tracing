from distributed_tracing.policies.policy_09 import DEFAULT_POLICY_09


def test_policy_09_describe():
    d = DEFAULT_POLICY_09.describe()
    assert d["index"] == 9
    assert DEFAULT_POLICY_09.breaker().name == "policy_09"


def test_policy_09_retry():
    r = DEFAULT_POLICY_09.retry()
    assert r.max_attempts >= 2
