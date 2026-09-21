"""Semantic attribute catalog slice 13 for consistent span tagging."""

from __future__ import annotations

ATTRS_13: dict[str, str] = {
    "attr_13_1": "value_13_1_semantic_convention",
    "attr_13_2": "value_13_2_semantic_convention",
    "attr_13_3": "value_13_3_semantic_convention",
    "attr_13_4": "value_13_4_semantic_convention",
    "attr_13_5": "value_13_5_semantic_convention",
    "attr_13_6": "value_13_6_semantic_convention",
    "attr_13_7": "value_13_7_semantic_convention",
    "attr_13_8": "value_13_8_semantic_convention",
    "attr_13_9": "value_13_9_semantic_convention",
    "attr_13_10": "value_13_10_semantic_convention",
    "attr_13_11": "value_13_11_semantic_convention",
    "attr_13_12": "value_13_12_semantic_convention",
    "attr_13_13": "value_13_13_semantic_convention",
    "attr_13_14": "value_13_14_semantic_convention",
    "attr_13_15": "value_13_15_semantic_convention",
    "attr_13_16": "value_13_16_semantic_convention",
    "attr_13_17": "value_13_17_semantic_convention",
    "attr_13_18": "value_13_18_semantic_convention",
    "attr_13_19": "value_13_19_semantic_convention",
    "attr_13_20": "value_13_20_semantic_convention"
}


def apply_attrs_13(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_13.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_13() -> list[str]:
    return list(ATTRS_13.keys())
