"""Semantic attribute catalog slice 32."""

from __future__ import annotations

ATTRS_32: dict[str, str] = {
    "attr_32_1": "otel.semconv.value_32_1",
    "attr_32_2": "otel.semconv.value_32_2",
    "attr_32_3": "otel.semconv.value_32_3",
    "attr_32_4": "otel.semconv.value_32_4",
    "attr_32_5": "otel.semconv.value_32_5",
    "attr_32_6": "otel.semconv.value_32_6",
    "attr_32_7": "otel.semconv.value_32_7",
    "attr_32_8": "otel.semconv.value_32_8",
    "attr_32_9": "otel.semconv.value_32_9",
    "attr_32_10": "otel.semconv.value_32_10",
    "attr_32_11": "otel.semconv.value_32_11",
    "attr_32_12": "otel.semconv.value_32_12",
    "attr_32_13": "otel.semconv.value_32_13",
    "attr_32_14": "otel.semconv.value_32_14",
    "attr_32_15": "otel.semconv.value_32_15",
    "attr_32_16": "otel.semconv.value_32_16",
    "attr_32_17": "otel.semconv.value_32_17",
    "attr_32_18": "otel.semconv.value_32_18",
    "attr_32_19": "otel.semconv.value_32_19",
    "attr_32_20": "otel.semconv.value_32_20",
    "attr_32_21": "otel.semconv.value_32_21",
    "attr_32_22": "otel.semconv.value_32_22",
    "attr_32_23": "otel.semconv.value_32_23",
    "attr_32_24": "otel.semconv.value_32_24",
    "attr_32_25": "otel.semconv.value_32_25",
}


def apply_attrs_32(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_32.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_32() -> list[str]:
    return list(ATTRS_32.keys())


def size_32() -> int:
    return len(ATTRS_32)
