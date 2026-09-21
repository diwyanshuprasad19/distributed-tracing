"""Semantic attribute catalog slice 07 for consistent span tagging."""

from __future__ import annotations

ATTRS_07: dict[str, str] = {
    "attr_7_1": "value_7_1_semantic_convention",
    "attr_7_2": "value_7_2_semantic_convention",
    "attr_7_3": "value_7_3_semantic_convention",
    "attr_7_4": "value_7_4_semantic_convention",
    "attr_7_5": "value_7_5_semantic_convention",
    "attr_7_6": "value_7_6_semantic_convention",
    "attr_7_7": "value_7_7_semantic_convention",
    "attr_7_8": "value_7_8_semantic_convention",
    "attr_7_9": "value_7_9_semantic_convention",
    "attr_7_10": "value_7_10_semantic_convention",
    "attr_7_11": "value_7_11_semantic_convention",
    "attr_7_12": "value_7_12_semantic_convention",
    "attr_7_13": "value_7_13_semantic_convention",
    "attr_7_14": "value_7_14_semantic_convention",
    "attr_7_15": "value_7_15_semantic_convention",
    "attr_7_16": "value_7_16_semantic_convention",
    "attr_7_17": "value_7_17_semantic_convention",
    "attr_7_18": "value_7_18_semantic_convention",
    "attr_7_19": "value_7_19_semantic_convention",
    "attr_7_20": "value_7_20_semantic_convention"
}


def apply_attrs_07(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_07.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_07() -> list[str]:
    return list(ATTRS_07.keys())
