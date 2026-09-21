"""Semantic attribute catalog slice 41."""

from __future__ import annotations

ATTRS_41: dict[str, str] = {
    "attr_41_1": "otel.semconv.value_41_1",
    "attr_41_2": "otel.semconv.value_41_2",
    "attr_41_3": "otel.semconv.value_41_3",
    "attr_41_4": "otel.semconv.value_41_4",
    "attr_41_5": "otel.semconv.value_41_5",
    "attr_41_6": "otel.semconv.value_41_6",
    "attr_41_7": "otel.semconv.value_41_7",
    "attr_41_8": "otel.semconv.value_41_8",
    "attr_41_9": "otel.semconv.value_41_9",
    "attr_41_10": "otel.semconv.value_41_10",
    "attr_41_11": "otel.semconv.value_41_11",
    "attr_41_12": "otel.semconv.value_41_12",
    "attr_41_13": "otel.semconv.value_41_13",
    "attr_41_14": "otel.semconv.value_41_14",
    "attr_41_15": "otel.semconv.value_41_15",
    "attr_41_16": "otel.semconv.value_41_16",
    "attr_41_17": "otel.semconv.value_41_17",
    "attr_41_18": "otel.semconv.value_41_18",
    "attr_41_19": "otel.semconv.value_41_19",
    "attr_41_20": "otel.semconv.value_41_20",
    "attr_41_21": "otel.semconv.value_41_21",
    "attr_41_22": "otel.semconv.value_41_22",
    "attr_41_23": "otel.semconv.value_41_23",
    "attr_41_24": "otel.semconv.value_41_24",
    "attr_41_25": "otel.semconv.value_41_25",
}


def apply_attrs_41(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_41.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_41() -> list[str]:
    return list(ATTRS_41.keys())


def size_41() -> int:
    return len(ATTRS_41)
