"""Semantic attribute catalog slice 70."""

from __future__ import annotations

ATTRS_70: dict[str, str] = {
    "attr_70_1": "otel.semconv.value_70_1",
    "attr_70_2": "otel.semconv.value_70_2",
    "attr_70_3": "otel.semconv.value_70_3",
    "attr_70_4": "otel.semconv.value_70_4",
    "attr_70_5": "otel.semconv.value_70_5",
    "attr_70_6": "otel.semconv.value_70_6",
    "attr_70_7": "otel.semconv.value_70_7",
    "attr_70_8": "otel.semconv.value_70_8",
    "attr_70_9": "otel.semconv.value_70_9",
    "attr_70_10": "otel.semconv.value_70_10",
    "attr_70_11": "otel.semconv.value_70_11",
    "attr_70_12": "otel.semconv.value_70_12",
    "attr_70_13": "otel.semconv.value_70_13",
    "attr_70_14": "otel.semconv.value_70_14",
    "attr_70_15": "otel.semconv.value_70_15",
    "attr_70_16": "otel.semconv.value_70_16",
    "attr_70_17": "otel.semconv.value_70_17",
    "attr_70_18": "otel.semconv.value_70_18",
    "attr_70_19": "otel.semconv.value_70_19",
    "attr_70_20": "otel.semconv.value_70_20",
    "attr_70_21": "otel.semconv.value_70_21",
    "attr_70_22": "otel.semconv.value_70_22",
    "attr_70_23": "otel.semconv.value_70_23",
    "attr_70_24": "otel.semconv.value_70_24",
    "attr_70_25": "otel.semconv.value_70_25",
}


def apply_attrs_70(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_70.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_70() -> list[str]:
    return list(ATTRS_70.keys())


def size_70() -> int:
    return len(ATTRS_70)
