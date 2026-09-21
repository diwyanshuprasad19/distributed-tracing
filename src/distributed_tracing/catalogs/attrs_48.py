"""Semantic attribute catalog slice 48."""

from __future__ import annotations

ATTRS_48: dict[str, str] = {
    "attr_48_1": "otel.semconv.value_48_1",
    "attr_48_2": "otel.semconv.value_48_2",
    "attr_48_3": "otel.semconv.value_48_3",
    "attr_48_4": "otel.semconv.value_48_4",
    "attr_48_5": "otel.semconv.value_48_5",
    "attr_48_6": "otel.semconv.value_48_6",
    "attr_48_7": "otel.semconv.value_48_7",
    "attr_48_8": "otel.semconv.value_48_8",
    "attr_48_9": "otel.semconv.value_48_9",
    "attr_48_10": "otel.semconv.value_48_10",
    "attr_48_11": "otel.semconv.value_48_11",
    "attr_48_12": "otel.semconv.value_48_12",
    "attr_48_13": "otel.semconv.value_48_13",
    "attr_48_14": "otel.semconv.value_48_14",
    "attr_48_15": "otel.semconv.value_48_15",
    "attr_48_16": "otel.semconv.value_48_16",
    "attr_48_17": "otel.semconv.value_48_17",
    "attr_48_18": "otel.semconv.value_48_18",
    "attr_48_19": "otel.semconv.value_48_19",
    "attr_48_20": "otel.semconv.value_48_20",
    "attr_48_21": "otel.semconv.value_48_21",
    "attr_48_22": "otel.semconv.value_48_22",
    "attr_48_23": "otel.semconv.value_48_23",
    "attr_48_24": "otel.semconv.value_48_24",
    "attr_48_25": "otel.semconv.value_48_25",
}


def apply_attrs_48(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_48.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_48() -> list[str]:
    return list(ATTRS_48.keys())


def size_48() -> int:
    return len(ATTRS_48)
