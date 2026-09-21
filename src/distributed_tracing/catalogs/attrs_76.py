"""Semantic attribute catalog slice 76."""

from __future__ import annotations

ATTRS_76: dict[str, str] = {
    "attr_76_1": "otel.semconv.value_76_1",
    "attr_76_2": "otel.semconv.value_76_2",
    "attr_76_3": "otel.semconv.value_76_3",
    "attr_76_4": "otel.semconv.value_76_4",
    "attr_76_5": "otel.semconv.value_76_5",
    "attr_76_6": "otel.semconv.value_76_6",
    "attr_76_7": "otel.semconv.value_76_7",
    "attr_76_8": "otel.semconv.value_76_8",
    "attr_76_9": "otel.semconv.value_76_9",
    "attr_76_10": "otel.semconv.value_76_10",
    "attr_76_11": "otel.semconv.value_76_11",
    "attr_76_12": "otel.semconv.value_76_12",
    "attr_76_13": "otel.semconv.value_76_13",
    "attr_76_14": "otel.semconv.value_76_14",
    "attr_76_15": "otel.semconv.value_76_15",
    "attr_76_16": "otel.semconv.value_76_16",
    "attr_76_17": "otel.semconv.value_76_17",
    "attr_76_18": "otel.semconv.value_76_18",
    "attr_76_19": "otel.semconv.value_76_19",
    "attr_76_20": "otel.semconv.value_76_20",
    "attr_76_21": "otel.semconv.value_76_21",
    "attr_76_22": "otel.semconv.value_76_22",
    "attr_76_23": "otel.semconv.value_76_23",
    "attr_76_24": "otel.semconv.value_76_24",
    "attr_76_25": "otel.semconv.value_76_25",
}


def apply_attrs_76(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_76.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_76() -> list[str]:
    return list(ATTRS_76.keys())


def size_76() -> int:
    return len(ATTRS_76)
