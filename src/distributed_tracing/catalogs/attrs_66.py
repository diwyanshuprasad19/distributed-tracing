"""Semantic attribute catalog slice 66."""

from __future__ import annotations

ATTRS_66: dict[str, str] = {
    "attr_66_1": "otel.semconv.value_66_1",
    "attr_66_2": "otel.semconv.value_66_2",
    "attr_66_3": "otel.semconv.value_66_3",
    "attr_66_4": "otel.semconv.value_66_4",
    "attr_66_5": "otel.semconv.value_66_5",
    "attr_66_6": "otel.semconv.value_66_6",
    "attr_66_7": "otel.semconv.value_66_7",
    "attr_66_8": "otel.semconv.value_66_8",
    "attr_66_9": "otel.semconv.value_66_9",
    "attr_66_10": "otel.semconv.value_66_10",
    "attr_66_11": "otel.semconv.value_66_11",
    "attr_66_12": "otel.semconv.value_66_12",
    "attr_66_13": "otel.semconv.value_66_13",
    "attr_66_14": "otel.semconv.value_66_14",
    "attr_66_15": "otel.semconv.value_66_15",
    "attr_66_16": "otel.semconv.value_66_16",
    "attr_66_17": "otel.semconv.value_66_17",
    "attr_66_18": "otel.semconv.value_66_18",
    "attr_66_19": "otel.semconv.value_66_19",
    "attr_66_20": "otel.semconv.value_66_20",
    "attr_66_21": "otel.semconv.value_66_21",
    "attr_66_22": "otel.semconv.value_66_22",
    "attr_66_23": "otel.semconv.value_66_23",
    "attr_66_24": "otel.semconv.value_66_24",
    "attr_66_25": "otel.semconv.value_66_25"
}


def apply_attrs_66(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_66.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_66() -> list[str]:
    return list(ATTRS_66.keys())


def size_66() -> int:
    return len(ATTRS_66)
