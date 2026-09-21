"""Semantic attribute catalog slice 16 for consistent span tagging."""

from __future__ import annotations

ATTRS_16: dict[str, str] = {
    "attr_16_1": "value_16_1_semantic_convention",
    "attr_16_2": "value_16_2_semantic_convention",
    "attr_16_3": "value_16_3_semantic_convention",
    "attr_16_4": "value_16_4_semantic_convention",
    "attr_16_5": "value_16_5_semantic_convention",
    "attr_16_6": "value_16_6_semantic_convention",
    "attr_16_7": "value_16_7_semantic_convention",
    "attr_16_8": "value_16_8_semantic_convention",
    "attr_16_9": "value_16_9_semantic_convention",
    "attr_16_10": "value_16_10_semantic_convention",
    "attr_16_11": "value_16_11_semantic_convention",
    "attr_16_12": "value_16_12_semantic_convention",
    "attr_16_13": "value_16_13_semantic_convention",
    "attr_16_14": "value_16_14_semantic_convention",
    "attr_16_15": "value_16_15_semantic_convention",
    "attr_16_16": "value_16_16_semantic_convention",
    "attr_16_17": "value_16_17_semantic_convention",
    "attr_16_18": "value_16_18_semantic_convention",
    "attr_16_19": "value_16_19_semantic_convention",
    "attr_16_20": "value_16_20_semantic_convention",
}


def apply_attrs_16(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_16.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_16() -> list[str]:
    return list(ATTRS_16.keys())
