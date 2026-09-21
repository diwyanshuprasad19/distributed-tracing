"""Semantic attribute catalog slice 53."""

from __future__ import annotations

ATTRS_53: dict[str, str] = {
    "attr_53_1": "otel.semconv.value_53_1",
    "attr_53_2": "otel.semconv.value_53_2",
    "attr_53_3": "otel.semconv.value_53_3",
    "attr_53_4": "otel.semconv.value_53_4",
    "attr_53_5": "otel.semconv.value_53_5",
    "attr_53_6": "otel.semconv.value_53_6",
    "attr_53_7": "otel.semconv.value_53_7",
    "attr_53_8": "otel.semconv.value_53_8",
    "attr_53_9": "otel.semconv.value_53_9",
    "attr_53_10": "otel.semconv.value_53_10",
    "attr_53_11": "otel.semconv.value_53_11",
    "attr_53_12": "otel.semconv.value_53_12",
    "attr_53_13": "otel.semconv.value_53_13",
    "attr_53_14": "otel.semconv.value_53_14",
    "attr_53_15": "otel.semconv.value_53_15",
    "attr_53_16": "otel.semconv.value_53_16",
    "attr_53_17": "otel.semconv.value_53_17",
    "attr_53_18": "otel.semconv.value_53_18",
    "attr_53_19": "otel.semconv.value_53_19",
    "attr_53_20": "otel.semconv.value_53_20",
    "attr_53_21": "otel.semconv.value_53_21",
    "attr_53_22": "otel.semconv.value_53_22",
    "attr_53_23": "otel.semconv.value_53_23",
    "attr_53_24": "otel.semconv.value_53_24",
    "attr_53_25": "otel.semconv.value_53_25",
}


def apply_attrs_53(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_53.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_53() -> list[str]:
    return list(ATTRS_53.keys())


def size_53() -> int:
    return len(ATTRS_53)
