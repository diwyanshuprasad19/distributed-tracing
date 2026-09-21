"""Semantic attribute catalog slice 40."""

from __future__ import annotations

ATTRS_40: dict[str, str] = {
    "attr_40_1": "otel.semconv.value_40_1",
    "attr_40_2": "otel.semconv.value_40_2",
    "attr_40_3": "otel.semconv.value_40_3",
    "attr_40_4": "otel.semconv.value_40_4",
    "attr_40_5": "otel.semconv.value_40_5",
    "attr_40_6": "otel.semconv.value_40_6",
    "attr_40_7": "otel.semconv.value_40_7",
    "attr_40_8": "otel.semconv.value_40_8",
    "attr_40_9": "otel.semconv.value_40_9",
    "attr_40_10": "otel.semconv.value_40_10",
    "attr_40_11": "otel.semconv.value_40_11",
    "attr_40_12": "otel.semconv.value_40_12",
    "attr_40_13": "otel.semconv.value_40_13",
    "attr_40_14": "otel.semconv.value_40_14",
    "attr_40_15": "otel.semconv.value_40_15",
    "attr_40_16": "otel.semconv.value_40_16",
    "attr_40_17": "otel.semconv.value_40_17",
    "attr_40_18": "otel.semconv.value_40_18",
    "attr_40_19": "otel.semconv.value_40_19",
    "attr_40_20": "otel.semconv.value_40_20",
    "attr_40_21": "otel.semconv.value_40_21",
    "attr_40_22": "otel.semconv.value_40_22",
    "attr_40_23": "otel.semconv.value_40_23",
    "attr_40_24": "otel.semconv.value_40_24",
    "attr_40_25": "otel.semconv.value_40_25"
}


def apply_attrs_40(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_40.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_40() -> list[str]:
    return list(ATTRS_40.keys())


def size_40() -> int:
    return len(ATTRS_40)
