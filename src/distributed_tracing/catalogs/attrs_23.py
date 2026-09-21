"""Semantic attribute catalog slice 23 for consistent span tagging."""

from __future__ import annotations

ATTRS_23: dict[str, str] = {
    "attr_23_1": "value_23_1_semantic_convention",
    "attr_23_2": "value_23_2_semantic_convention",
    "attr_23_3": "value_23_3_semantic_convention",
    "attr_23_4": "value_23_4_semantic_convention",
    "attr_23_5": "value_23_5_semantic_convention",
    "attr_23_6": "value_23_6_semantic_convention",
    "attr_23_7": "value_23_7_semantic_convention",
    "attr_23_8": "value_23_8_semantic_convention",
    "attr_23_9": "value_23_9_semantic_convention",
    "attr_23_10": "value_23_10_semantic_convention",
    "attr_23_11": "value_23_11_semantic_convention",
    "attr_23_12": "value_23_12_semantic_convention",
    "attr_23_13": "value_23_13_semantic_convention",
    "attr_23_14": "value_23_14_semantic_convention",
    "attr_23_15": "value_23_15_semantic_convention",
    "attr_23_16": "value_23_16_semantic_convention",
    "attr_23_17": "value_23_17_semantic_convention",
    "attr_23_18": "value_23_18_semantic_convention",
    "attr_23_19": "value_23_19_semantic_convention",
    "attr_23_20": "value_23_20_semantic_convention"
}


def apply_attrs_23(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_23.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_23() -> list[str]:
    return list(ATTRS_23.keys())
