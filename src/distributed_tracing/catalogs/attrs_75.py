"""Semantic attribute catalog slice 75."""

from __future__ import annotations

ATTRS_75: dict[str, str] = {
    "attr_75_1": "otel.semconv.value_75_1",
    "attr_75_2": "otel.semconv.value_75_2",
    "attr_75_3": "otel.semconv.value_75_3",
    "attr_75_4": "otel.semconv.value_75_4",
    "attr_75_5": "otel.semconv.value_75_5",
    "attr_75_6": "otel.semconv.value_75_6",
    "attr_75_7": "otel.semconv.value_75_7",
    "attr_75_8": "otel.semconv.value_75_8",
    "attr_75_9": "otel.semconv.value_75_9",
    "attr_75_10": "otel.semconv.value_75_10",
    "attr_75_11": "otel.semconv.value_75_11",
    "attr_75_12": "otel.semconv.value_75_12",
    "attr_75_13": "otel.semconv.value_75_13",
    "attr_75_14": "otel.semconv.value_75_14",
    "attr_75_15": "otel.semconv.value_75_15",
    "attr_75_16": "otel.semconv.value_75_16",
    "attr_75_17": "otel.semconv.value_75_17",
    "attr_75_18": "otel.semconv.value_75_18",
    "attr_75_19": "otel.semconv.value_75_19",
    "attr_75_20": "otel.semconv.value_75_20",
    "attr_75_21": "otel.semconv.value_75_21",
    "attr_75_22": "otel.semconv.value_75_22",
    "attr_75_23": "otel.semconv.value_75_23",
    "attr_75_24": "otel.semconv.value_75_24",
    "attr_75_25": "otel.semconv.value_75_25",
}


def apply_attrs_75(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_75.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_75() -> list[str]:
    return list(ATTRS_75.keys())


def size_75() -> int:
    return len(ATTRS_75)
