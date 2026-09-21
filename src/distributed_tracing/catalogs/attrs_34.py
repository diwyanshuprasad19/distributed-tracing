"""Semantic attribute catalog slice 34."""

from __future__ import annotations

ATTRS_34: dict[str, str] = {
    "attr_34_1": "otel.semconv.value_34_1",
    "attr_34_2": "otel.semconv.value_34_2",
    "attr_34_3": "otel.semconv.value_34_3",
    "attr_34_4": "otel.semconv.value_34_4",
    "attr_34_5": "otel.semconv.value_34_5",
    "attr_34_6": "otel.semconv.value_34_6",
    "attr_34_7": "otel.semconv.value_34_7",
    "attr_34_8": "otel.semconv.value_34_8",
    "attr_34_9": "otel.semconv.value_34_9",
    "attr_34_10": "otel.semconv.value_34_10",
    "attr_34_11": "otel.semconv.value_34_11",
    "attr_34_12": "otel.semconv.value_34_12",
    "attr_34_13": "otel.semconv.value_34_13",
    "attr_34_14": "otel.semconv.value_34_14",
    "attr_34_15": "otel.semconv.value_34_15",
    "attr_34_16": "otel.semconv.value_34_16",
    "attr_34_17": "otel.semconv.value_34_17",
    "attr_34_18": "otel.semconv.value_34_18",
    "attr_34_19": "otel.semconv.value_34_19",
    "attr_34_20": "otel.semconv.value_34_20",
    "attr_34_21": "otel.semconv.value_34_21",
    "attr_34_22": "otel.semconv.value_34_22",
    "attr_34_23": "otel.semconv.value_34_23",
    "attr_34_24": "otel.semconv.value_34_24",
    "attr_34_25": "otel.semconv.value_34_25",
}


def apply_attrs_34(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_34.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_34() -> list[str]:
    return list(ATTRS_34.keys())


def size_34() -> int:
    return len(ATTRS_34)
