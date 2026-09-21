"""Semantic attribute catalog slice 74."""

from __future__ import annotations

ATTRS_74: dict[str, str] = {
    "attr_74_1": "otel.semconv.value_74_1",
    "attr_74_2": "otel.semconv.value_74_2",
    "attr_74_3": "otel.semconv.value_74_3",
    "attr_74_4": "otel.semconv.value_74_4",
    "attr_74_5": "otel.semconv.value_74_5",
    "attr_74_6": "otel.semconv.value_74_6",
    "attr_74_7": "otel.semconv.value_74_7",
    "attr_74_8": "otel.semconv.value_74_8",
    "attr_74_9": "otel.semconv.value_74_9",
    "attr_74_10": "otel.semconv.value_74_10",
    "attr_74_11": "otel.semconv.value_74_11",
    "attr_74_12": "otel.semconv.value_74_12",
    "attr_74_13": "otel.semconv.value_74_13",
    "attr_74_14": "otel.semconv.value_74_14",
    "attr_74_15": "otel.semconv.value_74_15",
    "attr_74_16": "otel.semconv.value_74_16",
    "attr_74_17": "otel.semconv.value_74_17",
    "attr_74_18": "otel.semconv.value_74_18",
    "attr_74_19": "otel.semconv.value_74_19",
    "attr_74_20": "otel.semconv.value_74_20",
    "attr_74_21": "otel.semconv.value_74_21",
    "attr_74_22": "otel.semconv.value_74_22",
    "attr_74_23": "otel.semconv.value_74_23",
    "attr_74_24": "otel.semconv.value_74_24",
    "attr_74_25": "otel.semconv.value_74_25"
}


def apply_attrs_74(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_74.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_74() -> list[str]:
    return list(ATTRS_74.keys())


def size_74() -> int:
    return len(ATTRS_74)
