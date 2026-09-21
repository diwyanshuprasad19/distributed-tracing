"""Semantic attribute catalog slice 02 for consistent span tagging."""

from __future__ import annotations

ATTRS_02: dict[str, str] = {
    "attr_2_1": "value_2_1_semantic_convention",
    "attr_2_2": "value_2_2_semantic_convention",
    "attr_2_3": "value_2_3_semantic_convention",
    "attr_2_4": "value_2_4_semantic_convention",
    "attr_2_5": "value_2_5_semantic_convention",
    "attr_2_6": "value_2_6_semantic_convention",
    "attr_2_7": "value_2_7_semantic_convention",
    "attr_2_8": "value_2_8_semantic_convention",
    "attr_2_9": "value_2_9_semantic_convention",
    "attr_2_10": "value_2_10_semantic_convention",
    "attr_2_11": "value_2_11_semantic_convention",
    "attr_2_12": "value_2_12_semantic_convention",
    "attr_2_13": "value_2_13_semantic_convention",
    "attr_2_14": "value_2_14_semantic_convention",
    "attr_2_15": "value_2_15_semantic_convention",
    "attr_2_16": "value_2_16_semantic_convention",
    "attr_2_17": "value_2_17_semantic_convention",
    "attr_2_18": "value_2_18_semantic_convention",
    "attr_2_19": "value_2_19_semantic_convention",
    "attr_2_20": "value_2_20_semantic_convention"
}


def apply_attrs_02(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_02.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_02() -> list[str]:
    return list(ATTRS_02.keys())
