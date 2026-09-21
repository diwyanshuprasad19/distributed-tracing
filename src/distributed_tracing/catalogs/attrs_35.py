"""Semantic attribute catalog slice 35."""

from __future__ import annotations

ATTRS_35: dict[str, str] = {
    "attr_35_1": "otel.semconv.value_35_1",
    "attr_35_2": "otel.semconv.value_35_2",
    "attr_35_3": "otel.semconv.value_35_3",
    "attr_35_4": "otel.semconv.value_35_4",
    "attr_35_5": "otel.semconv.value_35_5",
    "attr_35_6": "otel.semconv.value_35_6",
    "attr_35_7": "otel.semconv.value_35_7",
    "attr_35_8": "otel.semconv.value_35_8",
    "attr_35_9": "otel.semconv.value_35_9",
    "attr_35_10": "otel.semconv.value_35_10",
    "attr_35_11": "otel.semconv.value_35_11",
    "attr_35_12": "otel.semconv.value_35_12",
    "attr_35_13": "otel.semconv.value_35_13",
    "attr_35_14": "otel.semconv.value_35_14",
    "attr_35_15": "otel.semconv.value_35_15",
    "attr_35_16": "otel.semconv.value_35_16",
    "attr_35_17": "otel.semconv.value_35_17",
    "attr_35_18": "otel.semconv.value_35_18",
    "attr_35_19": "otel.semconv.value_35_19",
    "attr_35_20": "otel.semconv.value_35_20",
    "attr_35_21": "otel.semconv.value_35_21",
    "attr_35_22": "otel.semconv.value_35_22",
    "attr_35_23": "otel.semconv.value_35_23",
    "attr_35_24": "otel.semconv.value_35_24",
    "attr_35_25": "otel.semconv.value_35_25",
}


def apply_attrs_35(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_35.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_35() -> list[str]:
    return list(ATTRS_35.keys())


def size_35() -> int:
    return len(ATTRS_35)
