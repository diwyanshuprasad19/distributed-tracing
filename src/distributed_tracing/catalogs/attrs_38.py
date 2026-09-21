"""Semantic attribute catalog slice 38."""

from __future__ import annotations

ATTRS_38: dict[str, str] = {
    "attr_38_1": "otel.semconv.value_38_1",
    "attr_38_2": "otel.semconv.value_38_2",
    "attr_38_3": "otel.semconv.value_38_3",
    "attr_38_4": "otel.semconv.value_38_4",
    "attr_38_5": "otel.semconv.value_38_5",
    "attr_38_6": "otel.semconv.value_38_6",
    "attr_38_7": "otel.semconv.value_38_7",
    "attr_38_8": "otel.semconv.value_38_8",
    "attr_38_9": "otel.semconv.value_38_9",
    "attr_38_10": "otel.semconv.value_38_10",
    "attr_38_11": "otel.semconv.value_38_11",
    "attr_38_12": "otel.semconv.value_38_12",
    "attr_38_13": "otel.semconv.value_38_13",
    "attr_38_14": "otel.semconv.value_38_14",
    "attr_38_15": "otel.semconv.value_38_15",
    "attr_38_16": "otel.semconv.value_38_16",
    "attr_38_17": "otel.semconv.value_38_17",
    "attr_38_18": "otel.semconv.value_38_18",
    "attr_38_19": "otel.semconv.value_38_19",
    "attr_38_20": "otel.semconv.value_38_20",
    "attr_38_21": "otel.semconv.value_38_21",
    "attr_38_22": "otel.semconv.value_38_22",
    "attr_38_23": "otel.semconv.value_38_23",
    "attr_38_24": "otel.semconv.value_38_24",
    "attr_38_25": "otel.semconv.value_38_25",
}


def apply_attrs_38(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_38.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_38() -> list[str]:
    return list(ATTRS_38.keys())


def size_38() -> int:
    return len(ATTRS_38)
