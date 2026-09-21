"""Semantic attribute catalog slice 62."""

from __future__ import annotations

ATTRS_62: dict[str, str] = {
    "attr_62_1": "otel.semconv.value_62_1",
    "attr_62_2": "otel.semconv.value_62_2",
    "attr_62_3": "otel.semconv.value_62_3",
    "attr_62_4": "otel.semconv.value_62_4",
    "attr_62_5": "otel.semconv.value_62_5",
    "attr_62_6": "otel.semconv.value_62_6",
    "attr_62_7": "otel.semconv.value_62_7",
    "attr_62_8": "otel.semconv.value_62_8",
    "attr_62_9": "otel.semconv.value_62_9",
    "attr_62_10": "otel.semconv.value_62_10",
    "attr_62_11": "otel.semconv.value_62_11",
    "attr_62_12": "otel.semconv.value_62_12",
    "attr_62_13": "otel.semconv.value_62_13",
    "attr_62_14": "otel.semconv.value_62_14",
    "attr_62_15": "otel.semconv.value_62_15",
    "attr_62_16": "otel.semconv.value_62_16",
    "attr_62_17": "otel.semconv.value_62_17",
    "attr_62_18": "otel.semconv.value_62_18",
    "attr_62_19": "otel.semconv.value_62_19",
    "attr_62_20": "otel.semconv.value_62_20",
    "attr_62_21": "otel.semconv.value_62_21",
    "attr_62_22": "otel.semconv.value_62_22",
    "attr_62_23": "otel.semconv.value_62_23",
    "attr_62_24": "otel.semconv.value_62_24",
    "attr_62_25": "otel.semconv.value_62_25",
}


def apply_attrs_62(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_62.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_62() -> list[str]:
    return list(ATTRS_62.keys())


def size_62() -> int:
    return len(ATTRS_62)
