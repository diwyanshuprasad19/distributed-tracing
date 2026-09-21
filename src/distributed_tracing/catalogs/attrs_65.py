"""Semantic attribute catalog slice 65."""

from __future__ import annotations

ATTRS_65: dict[str, str] = {
    "attr_65_1": "otel.semconv.value_65_1",
    "attr_65_2": "otel.semconv.value_65_2",
    "attr_65_3": "otel.semconv.value_65_3",
    "attr_65_4": "otel.semconv.value_65_4",
    "attr_65_5": "otel.semconv.value_65_5",
    "attr_65_6": "otel.semconv.value_65_6",
    "attr_65_7": "otel.semconv.value_65_7",
    "attr_65_8": "otel.semconv.value_65_8",
    "attr_65_9": "otel.semconv.value_65_9",
    "attr_65_10": "otel.semconv.value_65_10",
    "attr_65_11": "otel.semconv.value_65_11",
    "attr_65_12": "otel.semconv.value_65_12",
    "attr_65_13": "otel.semconv.value_65_13",
    "attr_65_14": "otel.semconv.value_65_14",
    "attr_65_15": "otel.semconv.value_65_15",
    "attr_65_16": "otel.semconv.value_65_16",
    "attr_65_17": "otel.semconv.value_65_17",
    "attr_65_18": "otel.semconv.value_65_18",
    "attr_65_19": "otel.semconv.value_65_19",
    "attr_65_20": "otel.semconv.value_65_20",
    "attr_65_21": "otel.semconv.value_65_21",
    "attr_65_22": "otel.semconv.value_65_22",
    "attr_65_23": "otel.semconv.value_65_23",
    "attr_65_24": "otel.semconv.value_65_24",
    "attr_65_25": "otel.semconv.value_65_25",
}


def apply_attrs_65(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_65.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_65() -> list[str]:
    return list(ATTRS_65.keys())


def size_65() -> int:
    return len(ATTRS_65)
