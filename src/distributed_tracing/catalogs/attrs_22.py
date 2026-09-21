"""Semantic attribute catalog slice 22 for consistent span tagging."""

from __future__ import annotations

ATTRS_22: dict[str, str] = {
    "attr_22_1": "value_22_1_semantic_convention",
    "attr_22_2": "value_22_2_semantic_convention",
    "attr_22_3": "value_22_3_semantic_convention",
    "attr_22_4": "value_22_4_semantic_convention",
    "attr_22_5": "value_22_5_semantic_convention",
    "attr_22_6": "value_22_6_semantic_convention",
    "attr_22_7": "value_22_7_semantic_convention",
    "attr_22_8": "value_22_8_semantic_convention",
    "attr_22_9": "value_22_9_semantic_convention",
    "attr_22_10": "value_22_10_semantic_convention",
    "attr_22_11": "value_22_11_semantic_convention",
    "attr_22_12": "value_22_12_semantic_convention",
    "attr_22_13": "value_22_13_semantic_convention",
    "attr_22_14": "value_22_14_semantic_convention",
    "attr_22_15": "value_22_15_semantic_convention",
    "attr_22_16": "value_22_16_semantic_convention",
    "attr_22_17": "value_22_17_semantic_convention",
    "attr_22_18": "value_22_18_semantic_convention",
    "attr_22_19": "value_22_19_semantic_convention",
    "attr_22_20": "value_22_20_semantic_convention"
}


def apply_attrs_22(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_22.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_22() -> list[str]:
    return list(ATTRS_22.keys())
