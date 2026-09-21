"""Semantic attribute catalog slice 18 for consistent span tagging."""

from __future__ import annotations

ATTRS_18: dict[str, str] = {
    "attr_18_1": "value_18_1_semantic_convention",
    "attr_18_2": "value_18_2_semantic_convention",
    "attr_18_3": "value_18_3_semantic_convention",
    "attr_18_4": "value_18_4_semantic_convention",
    "attr_18_5": "value_18_5_semantic_convention",
    "attr_18_6": "value_18_6_semantic_convention",
    "attr_18_7": "value_18_7_semantic_convention",
    "attr_18_8": "value_18_8_semantic_convention",
    "attr_18_9": "value_18_9_semantic_convention",
    "attr_18_10": "value_18_10_semantic_convention",
    "attr_18_11": "value_18_11_semantic_convention",
    "attr_18_12": "value_18_12_semantic_convention",
    "attr_18_13": "value_18_13_semantic_convention",
    "attr_18_14": "value_18_14_semantic_convention",
    "attr_18_15": "value_18_15_semantic_convention",
    "attr_18_16": "value_18_16_semantic_convention",
    "attr_18_17": "value_18_17_semantic_convention",
    "attr_18_18": "value_18_18_semantic_convention",
    "attr_18_19": "value_18_19_semantic_convention",
    "attr_18_20": "value_18_20_semantic_convention"
}


def apply_attrs_18(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_18.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_18() -> list[str]:
    return list(ATTRS_18.keys())
