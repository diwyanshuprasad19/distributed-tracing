.PHONY: test lint gate
test:
\tpytest -q
lint:
\truff check src tests || true
gate:
\tmake -C ../platform-ops local-gate REPO=distributed-tracing
\tmake -C ../platform-ops anti-slop REPO=distributed-tracing
