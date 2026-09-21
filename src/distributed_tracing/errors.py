"""Shared error taxonomy for traced services."""

from __future__ import annotations


class TracingError(Exception):
    """Base library error."""


class ConfigurationError(TracingError):
    """Invalid OTEL / breaker configuration."""


class ExportError(TracingError):
    """Span/metric export failed."""
