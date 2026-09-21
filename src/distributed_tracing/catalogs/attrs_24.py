"""Semantic attribute catalog slice 24 for consistent span tagging."""

from __future__ import annotations

ATTRS_24: dict[str, str] = {
    "attr_24_1": "value_24_1_semantic_convention",
    "attr_24_2": "value_24_2_semantic_convention",
    "attr_24_3": "value_24_3_semantic_convention",
    "attr_24_4": "value_24_4_semantic_convention",
    "attr_24_5": "value_24_5_semantic_convention",
    "attr_24_6": "value_24_6_semantic_convention",
    "attr_24_7": "value_24_7_semantic_convention",
    "attr_24_8": "value_24_8_semantic_convention",
    "attr_24_9": "value_24_9_semantic_convention",
    "attr_24_10": "value_24_10_semantic_convention",
    "attr_24_11": "value_24_11_semantic_convention",
    "attr_24_12": "value_24_12_semantic_convention",
    "attr_24_13": "value_24_13_semantic_convention",
    "attr_24_14": "value_24_14_semantic_convention",
    "attr_24_15": "value_24_15_semantic_convention",
    "attr_24_16": "value_24_16_semantic_convention",
    "attr_24_17": "value_24_17_semantic_convention",
    "attr_24_18": "value_24_18_semantic_convention",
    "attr_24_19": "value_24_19_semantic_convention",
    "attr_24_20": "value_24_20_semantic_convention"
}


def apply_attrs_24(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_24.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_24() -> list[str]:
    return list(ATTRS_24.keys())
