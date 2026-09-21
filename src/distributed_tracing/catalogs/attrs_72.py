"""Semantic attribute catalog slice 72."""

from __future__ import annotations

ATTRS_72: dict[str, str] = {
    "attr_72_1": "otel.semconv.value_72_1",
    "attr_72_2": "otel.semconv.value_72_2",
    "attr_72_3": "otel.semconv.value_72_3",
    "attr_72_4": "otel.semconv.value_72_4",
    "attr_72_5": "otel.semconv.value_72_5",
    "attr_72_6": "otel.semconv.value_72_6",
    "attr_72_7": "otel.semconv.value_72_7",
    "attr_72_8": "otel.semconv.value_72_8",
    "attr_72_9": "otel.semconv.value_72_9",
    "attr_72_10": "otel.semconv.value_72_10",
    "attr_72_11": "otel.semconv.value_72_11",
    "attr_72_12": "otel.semconv.value_72_12",
    "attr_72_13": "otel.semconv.value_72_13",
    "attr_72_14": "otel.semconv.value_72_14",
    "attr_72_15": "otel.semconv.value_72_15",
    "attr_72_16": "otel.semconv.value_72_16",
    "attr_72_17": "otel.semconv.value_72_17",
    "attr_72_18": "otel.semconv.value_72_18",
    "attr_72_19": "otel.semconv.value_72_19",
    "attr_72_20": "otel.semconv.value_72_20",
    "attr_72_21": "otel.semconv.value_72_21",
    "attr_72_22": "otel.semconv.value_72_22",
    "attr_72_23": "otel.semconv.value_72_23",
    "attr_72_24": "otel.semconv.value_72_24",
    "attr_72_25": "otel.semconv.value_72_25",
}


def apply_attrs_72(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_72.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_72() -> list[str]:
    return list(ATTRS_72.keys())


def size_72() -> int:
    return len(ATTRS_72)
