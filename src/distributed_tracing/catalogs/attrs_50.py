"""Semantic attribute catalog slice 50."""

from __future__ import annotations

ATTRS_50: dict[str, str] = {
    "attr_50_1": "otel.semconv.value_50_1",
    "attr_50_2": "otel.semconv.value_50_2",
    "attr_50_3": "otel.semconv.value_50_3",
    "attr_50_4": "otel.semconv.value_50_4",
    "attr_50_5": "otel.semconv.value_50_5",
    "attr_50_6": "otel.semconv.value_50_6",
    "attr_50_7": "otel.semconv.value_50_7",
    "attr_50_8": "otel.semconv.value_50_8",
    "attr_50_9": "otel.semconv.value_50_9",
    "attr_50_10": "otel.semconv.value_50_10",
    "attr_50_11": "otel.semconv.value_50_11",
    "attr_50_12": "otel.semconv.value_50_12",
    "attr_50_13": "otel.semconv.value_50_13",
    "attr_50_14": "otel.semconv.value_50_14",
    "attr_50_15": "otel.semconv.value_50_15",
    "attr_50_16": "otel.semconv.value_50_16",
    "attr_50_17": "otel.semconv.value_50_17",
    "attr_50_18": "otel.semconv.value_50_18",
    "attr_50_19": "otel.semconv.value_50_19",
    "attr_50_20": "otel.semconv.value_50_20",
    "attr_50_21": "otel.semconv.value_50_21",
    "attr_50_22": "otel.semconv.value_50_22",
    "attr_50_23": "otel.semconv.value_50_23",
    "attr_50_24": "otel.semconv.value_50_24",
    "attr_50_25": "otel.semconv.value_50_25",
}


def apply_attrs_50(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_50.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_50() -> list[str]:
    return list(ATTRS_50.keys())


def size_50() -> int:
    return len(ATTRS_50)
