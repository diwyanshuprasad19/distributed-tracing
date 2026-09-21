"""Semantic attribute catalog slice 64."""

from __future__ import annotations

ATTRS_64: dict[str, str] = {
    "attr_64_1": "otel.semconv.value_64_1",
    "attr_64_2": "otel.semconv.value_64_2",
    "attr_64_3": "otel.semconv.value_64_3",
    "attr_64_4": "otel.semconv.value_64_4",
    "attr_64_5": "otel.semconv.value_64_5",
    "attr_64_6": "otel.semconv.value_64_6",
    "attr_64_7": "otel.semconv.value_64_7",
    "attr_64_8": "otel.semconv.value_64_8",
    "attr_64_9": "otel.semconv.value_64_9",
    "attr_64_10": "otel.semconv.value_64_10",
    "attr_64_11": "otel.semconv.value_64_11",
    "attr_64_12": "otel.semconv.value_64_12",
    "attr_64_13": "otel.semconv.value_64_13",
    "attr_64_14": "otel.semconv.value_64_14",
    "attr_64_15": "otel.semconv.value_64_15",
    "attr_64_16": "otel.semconv.value_64_16",
    "attr_64_17": "otel.semconv.value_64_17",
    "attr_64_18": "otel.semconv.value_64_18",
    "attr_64_19": "otel.semconv.value_64_19",
    "attr_64_20": "otel.semconv.value_64_20",
    "attr_64_21": "otel.semconv.value_64_21",
    "attr_64_22": "otel.semconv.value_64_22",
    "attr_64_23": "otel.semconv.value_64_23",
    "attr_64_24": "otel.semconv.value_64_24",
    "attr_64_25": "otel.semconv.value_64_25",
}


def apply_attrs_64(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_64.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_64() -> list[str]:
    return list(ATTRS_64.keys())


def size_64() -> int:
    return len(ATTRS_64)
