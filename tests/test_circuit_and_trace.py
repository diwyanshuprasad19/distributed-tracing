from distributed_tracing import CircuitBreaker, CircuitOpenError, CircuitState, configure_tracing


def test_breaker_opens():
    b = CircuitBreaker(failure_threshold=2, recovery_timeout=60)
    for _ in range(2):
        try:
            b.call(lambda: (_ for _ in ()).throw(ConnectionError("x")))
        except ConnectionError:
            pass
    assert b.stats().state == CircuitState.OPEN
    try:
        b.call(lambda: 1)
        assert False
    except CircuitOpenError as e:
        assert e.retry_after >= 0


def test_configure_tracing_idempotent():
    p1 = configure_tracing("test-svc", endpoint="", console=True)
    p2 = configure_tracing("test-svc", endpoint="", console=True)
    assert p1 is p2
