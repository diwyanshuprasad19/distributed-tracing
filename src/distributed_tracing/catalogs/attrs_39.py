"""Semantic attribute catalog slice 39."""

from __future__ import annotations

ATTRS_39: dict[str, str] = {
    "attr_39_1": "otel.semconv.value_39_1",
    "attr_39_2": "otel.semconv.value_39_2",
    "attr_39_3": "otel.semconv.value_39_3",
    "attr_39_4": "otel.semconv.value_39_4",
    "attr_39_5": "otel.semconv.value_39_5",
    "attr_39_6": "otel.semconv.value_39_6",
    "attr_39_7": "otel.semconv.value_39_7",
    "attr_39_8": "otel.semconv.value_39_8",
    "attr_39_9": "otel.semconv.value_39_9",
    "attr_39_10": "otel.semconv.value_39_10",
    "attr_39_11": "otel.semconv.value_39_11",
    "attr_39_12": "otel.semconv.value_39_12",
    "attr_39_13": "otel.semconv.value_39_13",
    "attr_39_14": "otel.semconv.value_39_14",
    "attr_39_15": "otel.semconv.value_39_15",
    "attr_39_16": "otel.semconv.value_39_16",
    "attr_39_17": "otel.semconv.value_39_17",
    "attr_39_18": "otel.semconv.value_39_18",
    "attr_39_19": "otel.semconv.value_39_19",
    "attr_39_20": "otel.semconv.value_39_20",
    "attr_39_21": "otel.semconv.value_39_21",
    "attr_39_22": "otel.semconv.value_39_22",
    "attr_39_23": "otel.semconv.value_39_23",
    "attr_39_24": "otel.semconv.value_39_24",
    "attr_39_25": "otel.semconv.value_39_25",
}


def apply_attrs_39(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_39.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_39() -> list[str]:
    return list(ATTRS_39.keys())


def size_39() -> int:
    return len(ATTRS_39)
