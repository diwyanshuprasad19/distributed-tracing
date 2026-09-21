"""Semantic attribute catalog slice 31."""

from __future__ import annotations

ATTRS_31: dict[str, str] = {
    "attr_31_1": "otel.semconv.value_31_1",
    "attr_31_2": "otel.semconv.value_31_2",
    "attr_31_3": "otel.semconv.value_31_3",
    "attr_31_4": "otel.semconv.value_31_4",
    "attr_31_5": "otel.semconv.value_31_5",
    "attr_31_6": "otel.semconv.value_31_6",
    "attr_31_7": "otel.semconv.value_31_7",
    "attr_31_8": "otel.semconv.value_31_8",
    "attr_31_9": "otel.semconv.value_31_9",
    "attr_31_10": "otel.semconv.value_31_10",
    "attr_31_11": "otel.semconv.value_31_11",
    "attr_31_12": "otel.semconv.value_31_12",
    "attr_31_13": "otel.semconv.value_31_13",
    "attr_31_14": "otel.semconv.value_31_14",
    "attr_31_15": "otel.semconv.value_31_15",
    "attr_31_16": "otel.semconv.value_31_16",
    "attr_31_17": "otel.semconv.value_31_17",
    "attr_31_18": "otel.semconv.value_31_18",
    "attr_31_19": "otel.semconv.value_31_19",
    "attr_31_20": "otel.semconv.value_31_20",
    "attr_31_21": "otel.semconv.value_31_21",
    "attr_31_22": "otel.semconv.value_31_22",
    "attr_31_23": "otel.semconv.value_31_23",
    "attr_31_24": "otel.semconv.value_31_24",
    "attr_31_25": "otel.semconv.value_31_25"
}


def apply_attrs_31(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_31.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_31() -> list[str]:
    return list(ATTRS_31.keys())


def size_31() -> int:
    return len(ATTRS_31)
