"""Semantic attribute catalog slice 14 for consistent span tagging."""

from __future__ import annotations

ATTRS_14: dict[str, str] = {
    "attr_14_1": "value_14_1_semantic_convention",
    "attr_14_2": "value_14_2_semantic_convention",
    "attr_14_3": "value_14_3_semantic_convention",
    "attr_14_4": "value_14_4_semantic_convention",
    "attr_14_5": "value_14_5_semantic_convention",
    "attr_14_6": "value_14_6_semantic_convention",
    "attr_14_7": "value_14_7_semantic_convention",
    "attr_14_8": "value_14_8_semantic_convention",
    "attr_14_9": "value_14_9_semantic_convention",
    "attr_14_10": "value_14_10_semantic_convention",
    "attr_14_11": "value_14_11_semantic_convention",
    "attr_14_12": "value_14_12_semantic_convention",
    "attr_14_13": "value_14_13_semantic_convention",
    "attr_14_14": "value_14_14_semantic_convention",
    "attr_14_15": "value_14_15_semantic_convention",
    "attr_14_16": "value_14_16_semantic_convention",
    "attr_14_17": "value_14_17_semantic_convention",
    "attr_14_18": "value_14_18_semantic_convention",
    "attr_14_19": "value_14_19_semantic_convention",
    "attr_14_20": "value_14_20_semantic_convention"
}


def apply_attrs_14(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_14.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_14() -> list[str]:
    return list(ATTRS_14.keys())
