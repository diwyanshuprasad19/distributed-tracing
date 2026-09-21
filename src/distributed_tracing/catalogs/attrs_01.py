"""Semantic attribute catalog slice 01 for consistent span tagging."""

from __future__ import annotations

ATTRS_01: dict[str, str] = {
    "attr_1_1": "value_1_1_semantic_convention",
    "attr_1_2": "value_1_2_semantic_convention",
    "attr_1_3": "value_1_3_semantic_convention",
    "attr_1_4": "value_1_4_semantic_convention",
    "attr_1_5": "value_1_5_semantic_convention",
    "attr_1_6": "value_1_6_semantic_convention",
    "attr_1_7": "value_1_7_semantic_convention",
    "attr_1_8": "value_1_8_semantic_convention",
    "attr_1_9": "value_1_9_semantic_convention",
    "attr_1_10": "value_1_10_semantic_convention",
    "attr_1_11": "value_1_11_semantic_convention",
    "attr_1_12": "value_1_12_semantic_convention",
    "attr_1_13": "value_1_13_semantic_convention",
    "attr_1_14": "value_1_14_semantic_convention",
    "attr_1_15": "value_1_15_semantic_convention",
    "attr_1_16": "value_1_16_semantic_convention",
    "attr_1_17": "value_1_17_semantic_convention",
    "attr_1_18": "value_1_18_semantic_convention",
    "attr_1_19": "value_1_19_semantic_convention",
    "attr_1_20": "value_1_20_semantic_convention"
}


def apply_attrs_01(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_01.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_01() -> list[str]:
    return list(ATTRS_01.keys())
