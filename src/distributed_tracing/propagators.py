"""Composite propagators: W3C TraceContext + Baggage + optional B3."""

from __future__ import annotations

import os

from opentelemetry.baggage.propagation import W3CBaggagePropagator
from opentelemetry.propagate import set_global_textmap
from opentelemetry.propagators.composite import CompositePropagator
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator


def configure_propagators(*, enable_b3: bool | None = None) -> None:
    use_b3 = (
        enable_b3
        if enable_b3 is not None
        else os.getenv("OTEL_PROPAGATORS", "tracecontext,baggage").find("b3") >= 0
    )
    props = [TraceContextTextMapPropagator(), W3CBaggagePropagator()]
    if use_b3:
        try:
            from opentelemetry.propagators.b3 import B3MultiFormat

            props.append(B3MultiFormat())
        except Exception:  # pragma: no cover
            pass
    set_global_textmap(CompositePropagator(props))
