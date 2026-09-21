"""Semantic attribute catalog slice 80."""

from __future__ import annotations

ATTRS_80: dict[str, str] = {
    "attr_80_1": "otel.semconv.value_80_1",
    "attr_80_2": "otel.semconv.value_80_2",
    "attr_80_3": "otel.semconv.value_80_3",
    "attr_80_4": "otel.semconv.value_80_4",
    "attr_80_5": "otel.semconv.value_80_5",
    "attr_80_6": "otel.semconv.value_80_6",
    "attr_80_7": "otel.semconv.value_80_7",
    "attr_80_8": "otel.semconv.value_80_8",
    "attr_80_9": "otel.semconv.value_80_9",
    "attr_80_10": "otel.semconv.value_80_10",
    "attr_80_11": "otel.semconv.value_80_11",
    "attr_80_12": "otel.semconv.value_80_12",
    "attr_80_13": "otel.semconv.value_80_13",
    "attr_80_14": "otel.semconv.value_80_14",
    "attr_80_15": "otel.semconv.value_80_15",
    "attr_80_16": "otel.semconv.value_80_16",
    "attr_80_17": "otel.semconv.value_80_17",
    "attr_80_18": "otel.semconv.value_80_18",
    "attr_80_19": "otel.semconv.value_80_19",
    "attr_80_20": "otel.semconv.value_80_20",
    "attr_80_21": "otel.semconv.value_80_21",
    "attr_80_22": "otel.semconv.value_80_22",
    "attr_80_23": "otel.semconv.value_80_23",
    "attr_80_24": "otel.semconv.value_80_24",
    "attr_80_25": "otel.semconv.value_80_25",
}


def apply_attrs_80(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_80.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_80() -> list[str]:
    return list(ATTRS_80.keys())


def size_80() -> int:
    return len(ATTRS_80)
