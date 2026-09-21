"""Semantic attribute catalog slice 37."""

from __future__ import annotations

ATTRS_37: dict[str, str] = {
    "attr_37_1": "otel.semconv.value_37_1",
    "attr_37_2": "otel.semconv.value_37_2",
    "attr_37_3": "otel.semconv.value_37_3",
    "attr_37_4": "otel.semconv.value_37_4",
    "attr_37_5": "otel.semconv.value_37_5",
    "attr_37_6": "otel.semconv.value_37_6",
    "attr_37_7": "otel.semconv.value_37_7",
    "attr_37_8": "otel.semconv.value_37_8",
    "attr_37_9": "otel.semconv.value_37_9",
    "attr_37_10": "otel.semconv.value_37_10",
    "attr_37_11": "otel.semconv.value_37_11",
    "attr_37_12": "otel.semconv.value_37_12",
    "attr_37_13": "otel.semconv.value_37_13",
    "attr_37_14": "otel.semconv.value_37_14",
    "attr_37_15": "otel.semconv.value_37_15",
    "attr_37_16": "otel.semconv.value_37_16",
    "attr_37_17": "otel.semconv.value_37_17",
    "attr_37_18": "otel.semconv.value_37_18",
    "attr_37_19": "otel.semconv.value_37_19",
    "attr_37_20": "otel.semconv.value_37_20",
    "attr_37_21": "otel.semconv.value_37_21",
    "attr_37_22": "otel.semconv.value_37_22",
    "attr_37_23": "otel.semconv.value_37_23",
    "attr_37_24": "otel.semconv.value_37_24",
    "attr_37_25": "otel.semconv.value_37_25",
}


def apply_attrs_37(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_37.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_37() -> list[str]:
    return list(ATTRS_37.keys())


def size_37() -> int:
    return len(ATTRS_37)
