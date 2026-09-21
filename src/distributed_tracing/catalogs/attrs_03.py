"""Semantic attribute catalog slice 03 for consistent span tagging."""

from __future__ import annotations

ATTRS_03: dict[str, str] = {
    "attr_3_1": "value_3_1_semantic_convention",
    "attr_3_2": "value_3_2_semantic_convention",
    "attr_3_3": "value_3_3_semantic_convention",
    "attr_3_4": "value_3_4_semantic_convention",
    "attr_3_5": "value_3_5_semantic_convention",
    "attr_3_6": "value_3_6_semantic_convention",
    "attr_3_7": "value_3_7_semantic_convention",
    "attr_3_8": "value_3_8_semantic_convention",
    "attr_3_9": "value_3_9_semantic_convention",
    "attr_3_10": "value_3_10_semantic_convention",
    "attr_3_11": "value_3_11_semantic_convention",
    "attr_3_12": "value_3_12_semantic_convention",
    "attr_3_13": "value_3_13_semantic_convention",
    "attr_3_14": "value_3_14_semantic_convention",
    "attr_3_15": "value_3_15_semantic_convention",
    "attr_3_16": "value_3_16_semantic_convention",
    "attr_3_17": "value_3_17_semantic_convention",
    "attr_3_18": "value_3_18_semantic_convention",
    "attr_3_19": "value_3_19_semantic_convention",
    "attr_3_20": "value_3_20_semantic_convention"
}


def apply_attrs_03(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_03.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_03() -> list[str]:
    return list(ATTRS_03.keys())
