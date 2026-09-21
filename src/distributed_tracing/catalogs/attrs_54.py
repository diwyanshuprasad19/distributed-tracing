"""Semantic attribute catalog slice 54."""

from __future__ import annotations

ATTRS_54: dict[str, str] = {
    "attr_54_1": "otel.semconv.value_54_1",
    "attr_54_2": "otel.semconv.value_54_2",
    "attr_54_3": "otel.semconv.value_54_3",
    "attr_54_4": "otel.semconv.value_54_4",
    "attr_54_5": "otel.semconv.value_54_5",
    "attr_54_6": "otel.semconv.value_54_6",
    "attr_54_7": "otel.semconv.value_54_7",
    "attr_54_8": "otel.semconv.value_54_8",
    "attr_54_9": "otel.semconv.value_54_9",
    "attr_54_10": "otel.semconv.value_54_10",
    "attr_54_11": "otel.semconv.value_54_11",
    "attr_54_12": "otel.semconv.value_54_12",
    "attr_54_13": "otel.semconv.value_54_13",
    "attr_54_14": "otel.semconv.value_54_14",
    "attr_54_15": "otel.semconv.value_54_15",
    "attr_54_16": "otel.semconv.value_54_16",
    "attr_54_17": "otel.semconv.value_54_17",
    "attr_54_18": "otel.semconv.value_54_18",
    "attr_54_19": "otel.semconv.value_54_19",
    "attr_54_20": "otel.semconv.value_54_20",
    "attr_54_21": "otel.semconv.value_54_21",
    "attr_54_22": "otel.semconv.value_54_22",
    "attr_54_23": "otel.semconv.value_54_23",
    "attr_54_24": "otel.semconv.value_54_24",
    "attr_54_25": "otel.semconv.value_54_25",
}


def apply_attrs_54(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_54.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_54() -> list[str]:
    return list(ATTRS_54.keys())


def size_54() -> int:
    return len(ATTRS_54)
