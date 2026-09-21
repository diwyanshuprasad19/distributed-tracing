from distributed_tracing.policies.policy_08 import DEFAULT_POLICY_08


def test_policy_08_describe():
    d = DEFAULT_POLICY_08.describe()
    assert d["index"] == 8
    assert DEFAULT_POLICY_08.breaker().name == "policy_08"


def test_policy_08_retry():
    r = DEFAULT_POLICY_08.retry()
    assert r.max_attempts >= 2
