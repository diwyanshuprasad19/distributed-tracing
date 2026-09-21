"""Semantic attribute catalog slice 36."""

from __future__ import annotations

ATTRS_36: dict[str, str] = {
    "attr_36_1": "otel.semconv.value_36_1",
    "attr_36_2": "otel.semconv.value_36_2",
    "attr_36_3": "otel.semconv.value_36_3",
    "attr_36_4": "otel.semconv.value_36_4",
    "attr_36_5": "otel.semconv.value_36_5",
    "attr_36_6": "otel.semconv.value_36_6",
    "attr_36_7": "otel.semconv.value_36_7",
    "attr_36_8": "otel.semconv.value_36_8",
    "attr_36_9": "otel.semconv.value_36_9",
    "attr_36_10": "otel.semconv.value_36_10",
    "attr_36_11": "otel.semconv.value_36_11",
    "attr_36_12": "otel.semconv.value_36_12",
    "attr_36_13": "otel.semconv.value_36_13",
    "attr_36_14": "otel.semconv.value_36_14",
    "attr_36_15": "otel.semconv.value_36_15",
    "attr_36_16": "otel.semconv.value_36_16",
    "attr_36_17": "otel.semconv.value_36_17",
    "attr_36_18": "otel.semconv.value_36_18",
    "attr_36_19": "otel.semconv.value_36_19",
    "attr_36_20": "otel.semconv.value_36_20",
    "attr_36_21": "otel.semconv.value_36_21",
    "attr_36_22": "otel.semconv.value_36_22",
    "attr_36_23": "otel.semconv.value_36_23",
    "attr_36_24": "otel.semconv.value_36_24",
    "attr_36_25": "otel.semconv.value_36_25"
}


def apply_attrs_36(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_36.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_36() -> list[str]:
    return list(ATTRS_36.keys())


def size_36() -> int:
    return len(ATTRS_36)
