"""Semantic attribute catalog slice 06 for consistent span tagging."""

from __future__ import annotations

ATTRS_06: dict[str, str] = {
    "attr_6_1": "value_6_1_semantic_convention",
    "attr_6_2": "value_6_2_semantic_convention",
    "attr_6_3": "value_6_3_semantic_convention",
    "attr_6_4": "value_6_4_semantic_convention",
    "attr_6_5": "value_6_5_semantic_convention",
    "attr_6_6": "value_6_6_semantic_convention",
    "attr_6_7": "value_6_7_semantic_convention",
    "attr_6_8": "value_6_8_semantic_convention",
    "attr_6_9": "value_6_9_semantic_convention",
    "attr_6_10": "value_6_10_semantic_convention",
    "attr_6_11": "value_6_11_semantic_convention",
    "attr_6_12": "value_6_12_semantic_convention",
    "attr_6_13": "value_6_13_semantic_convention",
    "attr_6_14": "value_6_14_semantic_convention",
    "attr_6_15": "value_6_15_semantic_convention",
    "attr_6_16": "value_6_16_semantic_convention",
    "attr_6_17": "value_6_17_semantic_convention",
    "attr_6_18": "value_6_18_semantic_convention",
    "attr_6_19": "value_6_19_semantic_convention",
    "attr_6_20": "value_6_20_semantic_convention"
}


def apply_attrs_06(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_06.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_06() -> list[str]:
    return list(ATTRS_06.keys())
