"""Convenience span attribute helpers aligned with semantic conventions."""

from __future__ import annotations

from typing import Any

from opentelemetry.trace import Span


def set_http_attrs(span: Span, *, method: str, route: str, status: int) -> None:
    span.set_attribute("http.request.method", method)
    span.set_attribute("http.route", route)
    span.set_attribute("http.response.status_code", status)


def set_db_attrs(span: Span, *, system: str, statement: str, name: str) -> None:
    span.set_attribute("db.system", system)
    span.set_attribute("db.statement", statement[:512])
    span.set_attribute("db.name", name)


def set_rpc_attrs(span: Span, *, service: str, method: str) -> None:
    span.set_attribute("rpc.service", service)
    span.set_attribute("rpc.method", method)


def enrich(span: Span, attrs: dict[str, Any]) -> None:
    for k, v in attrs.items():
        if v is not None:
            span.set_attribute(k, v)
