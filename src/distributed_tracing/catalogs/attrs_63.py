"""Semantic attribute catalog slice 63."""

from __future__ import annotations

ATTRS_63: dict[str, str] = {
    "attr_63_1": "otel.semconv.value_63_1",
    "attr_63_2": "otel.semconv.value_63_2",
    "attr_63_3": "otel.semconv.value_63_3",
    "attr_63_4": "otel.semconv.value_63_4",
    "attr_63_5": "otel.semconv.value_63_5",
    "attr_63_6": "otel.semconv.value_63_6",
    "attr_63_7": "otel.semconv.value_63_7",
    "attr_63_8": "otel.semconv.value_63_8",
    "attr_63_9": "otel.semconv.value_63_9",
    "attr_63_10": "otel.semconv.value_63_10",
    "attr_63_11": "otel.semconv.value_63_11",
    "attr_63_12": "otel.semconv.value_63_12",
    "attr_63_13": "otel.semconv.value_63_13",
    "attr_63_14": "otel.semconv.value_63_14",
    "attr_63_15": "otel.semconv.value_63_15",
    "attr_63_16": "otel.semconv.value_63_16",
    "attr_63_17": "otel.semconv.value_63_17",
    "attr_63_18": "otel.semconv.value_63_18",
    "attr_63_19": "otel.semconv.value_63_19",
    "attr_63_20": "otel.semconv.value_63_20",
    "attr_63_21": "otel.semconv.value_63_21",
    "attr_63_22": "otel.semconv.value_63_22",
    "attr_63_23": "otel.semconv.value_63_23",
    "attr_63_24": "otel.semconv.value_63_24",
    "attr_63_25": "otel.semconv.value_63_25",
}


def apply_attrs_63(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_63.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_63() -> list[str]:
    return list(ATTRS_63.keys())


def size_63() -> int:
    return len(ATTRS_63)
