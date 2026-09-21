from distributed_tracing.policies.policy_02 import DEFAULT_POLICY_02


def test_policy_02_describe():
    d = DEFAULT_POLICY_02.describe()
    assert d["index"] == 2
    assert DEFAULT_POLICY_02.breaker().name == "policy_02"


def test_policy_02_retry():
    r = DEFAULT_POLICY_02.retry()
    assert r.max_attempts >= 2
