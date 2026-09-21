"""Semantic attribute catalog slice 60."""

from __future__ import annotations

ATTRS_60: dict[str, str] = {
    "attr_60_1": "otel.semconv.value_60_1",
    "attr_60_2": "otel.semconv.value_60_2",
    "attr_60_3": "otel.semconv.value_60_3",
    "attr_60_4": "otel.semconv.value_60_4",
    "attr_60_5": "otel.semconv.value_60_5",
    "attr_60_6": "otel.semconv.value_60_6",
    "attr_60_7": "otel.semconv.value_60_7",
    "attr_60_8": "otel.semconv.value_60_8",
    "attr_60_9": "otel.semconv.value_60_9",
    "attr_60_10": "otel.semconv.value_60_10",
    "attr_60_11": "otel.semconv.value_60_11",
    "attr_60_12": "otel.semconv.value_60_12",
    "attr_60_13": "otel.semconv.value_60_13",
    "attr_60_14": "otel.semconv.value_60_14",
    "attr_60_15": "otel.semconv.value_60_15",
    "attr_60_16": "otel.semconv.value_60_16",
    "attr_60_17": "otel.semconv.value_60_17",
    "attr_60_18": "otel.semconv.value_60_18",
    "attr_60_19": "otel.semconv.value_60_19",
    "attr_60_20": "otel.semconv.value_60_20",
    "attr_60_21": "otel.semconv.value_60_21",
    "attr_60_22": "otel.semconv.value_60_22",
    "attr_60_23": "otel.semconv.value_60_23",
    "attr_60_24": "otel.semconv.value_60_24",
    "attr_60_25": "otel.semconv.value_60_25"
}


def apply_attrs_60(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_60.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_60() -> list[str]:
    return list(ATTRS_60.keys())


def size_60() -> int:
    return len(ATTRS_60)
