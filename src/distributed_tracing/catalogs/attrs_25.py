"""Semantic attribute catalog slice 25 for consistent span tagging."""

from __future__ import annotations

ATTRS_25: dict[str, str] = {
    "attr_25_1": "value_25_1_semantic_convention",
    "attr_25_2": "value_25_2_semantic_convention",
    "attr_25_3": "value_25_3_semantic_convention",
    "attr_25_4": "value_25_4_semantic_convention",
    "attr_25_5": "value_25_5_semantic_convention",
    "attr_25_6": "value_25_6_semantic_convention",
    "attr_25_7": "value_25_7_semantic_convention",
    "attr_25_8": "value_25_8_semantic_convention",
    "attr_25_9": "value_25_9_semantic_convention",
    "attr_25_10": "value_25_10_semantic_convention",
    "attr_25_11": "value_25_11_semantic_convention",
    "attr_25_12": "value_25_12_semantic_convention",
    "attr_25_13": "value_25_13_semantic_convention",
    "attr_25_14": "value_25_14_semantic_convention",
    "attr_25_15": "value_25_15_semantic_convention",
    "attr_25_16": "value_25_16_semantic_convention",
    "attr_25_17": "value_25_17_semantic_convention",
    "attr_25_18": "value_25_18_semantic_convention",
    "attr_25_19": "value_25_19_semantic_convention",
    "attr_25_20": "value_25_20_semantic_convention",
}


def apply_attrs_25(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_25.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_25() -> list[str]:
    return list(ATTRS_25.keys())
