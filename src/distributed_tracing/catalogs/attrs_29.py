"""Semantic attribute catalog slice 29 for consistent span tagging."""

from __future__ import annotations

ATTRS_29: dict[str, str] = {
    "attr_29_1": "value_29_1_semantic_convention",
    "attr_29_2": "value_29_2_semantic_convention",
    "attr_29_3": "value_29_3_semantic_convention",
    "attr_29_4": "value_29_4_semantic_convention",
    "attr_29_5": "value_29_5_semantic_convention",
    "attr_29_6": "value_29_6_semantic_convention",
    "attr_29_7": "value_29_7_semantic_convention",
    "attr_29_8": "value_29_8_semantic_convention",
    "attr_29_9": "value_29_9_semantic_convention",
    "attr_29_10": "value_29_10_semantic_convention",
    "attr_29_11": "value_29_11_semantic_convention",
    "attr_29_12": "value_29_12_semantic_convention",
    "attr_29_13": "value_29_13_semantic_convention",
    "attr_29_14": "value_29_14_semantic_convention",
    "attr_29_15": "value_29_15_semantic_convention",
    "attr_29_16": "value_29_16_semantic_convention",
    "attr_29_17": "value_29_17_semantic_convention",
    "attr_29_18": "value_29_18_semantic_convention",
    "attr_29_19": "value_29_19_semantic_convention",
    "attr_29_20": "value_29_20_semantic_convention"
}


def apply_attrs_29(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_29.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_29() -> list[str]:
    return list(ATTRS_29.keys())
