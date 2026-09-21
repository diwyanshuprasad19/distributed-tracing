"""Semantic attribute catalog slice 04 for consistent span tagging."""

from __future__ import annotations

ATTRS_04: dict[str, str] = {
    "attr_4_1": "value_4_1_semantic_convention",
    "attr_4_2": "value_4_2_semantic_convention",
    "attr_4_3": "value_4_3_semantic_convention",
    "attr_4_4": "value_4_4_semantic_convention",
    "attr_4_5": "value_4_5_semantic_convention",
    "attr_4_6": "value_4_6_semantic_convention",
    "attr_4_7": "value_4_7_semantic_convention",
    "attr_4_8": "value_4_8_semantic_convention",
    "attr_4_9": "value_4_9_semantic_convention",
    "attr_4_10": "value_4_10_semantic_convention",
    "attr_4_11": "value_4_11_semantic_convention",
    "attr_4_12": "value_4_12_semantic_convention",
    "attr_4_13": "value_4_13_semantic_convention",
    "attr_4_14": "value_4_14_semantic_convention",
    "attr_4_15": "value_4_15_semantic_convention",
    "attr_4_16": "value_4_16_semantic_convention",
    "attr_4_17": "value_4_17_semantic_convention",
    "attr_4_18": "value_4_18_semantic_convention",
    "attr_4_19": "value_4_19_semantic_convention",
    "attr_4_20": "value_4_20_semantic_convention"
}


def apply_attrs_04(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_04.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_04() -> list[str]:
    return list(ATTRS_04.keys())
