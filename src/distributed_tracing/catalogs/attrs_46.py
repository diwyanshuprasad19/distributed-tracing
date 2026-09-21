"""Semantic attribute catalog slice 46."""

from __future__ import annotations

ATTRS_46: dict[str, str] = {
    "attr_46_1": "otel.semconv.value_46_1",
    "attr_46_2": "otel.semconv.value_46_2",
    "attr_46_3": "otel.semconv.value_46_3",
    "attr_46_4": "otel.semconv.value_46_4",
    "attr_46_5": "otel.semconv.value_46_5",
    "attr_46_6": "otel.semconv.value_46_6",
    "attr_46_7": "otel.semconv.value_46_7",
    "attr_46_8": "otel.semconv.value_46_8",
    "attr_46_9": "otel.semconv.value_46_9",
    "attr_46_10": "otel.semconv.value_46_10",
    "attr_46_11": "otel.semconv.value_46_11",
    "attr_46_12": "otel.semconv.value_46_12",
    "attr_46_13": "otel.semconv.value_46_13",
    "attr_46_14": "otel.semconv.value_46_14",
    "attr_46_15": "otel.semconv.value_46_15",
    "attr_46_16": "otel.semconv.value_46_16",
    "attr_46_17": "otel.semconv.value_46_17",
    "attr_46_18": "otel.semconv.value_46_18",
    "attr_46_19": "otel.semconv.value_46_19",
    "attr_46_20": "otel.semconv.value_46_20",
    "attr_46_21": "otel.semconv.value_46_21",
    "attr_46_22": "otel.semconv.value_46_22",
    "attr_46_23": "otel.semconv.value_46_23",
    "attr_46_24": "otel.semconv.value_46_24",
    "attr_46_25": "otel.semconv.value_46_25",
}


def apply_attrs_46(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_46.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_46() -> list[str]:
    return list(ATTRS_46.keys())


def size_46() -> int:
    return len(ATTRS_46)
