"""Semantic attribute catalog slice 15 for consistent span tagging."""

from __future__ import annotations

ATTRS_15: dict[str, str] = {
    "attr_15_1": "value_15_1_semantic_convention",
    "attr_15_2": "value_15_2_semantic_convention",
    "attr_15_3": "value_15_3_semantic_convention",
    "attr_15_4": "value_15_4_semantic_convention",
    "attr_15_5": "value_15_5_semantic_convention",
    "attr_15_6": "value_15_6_semantic_convention",
    "attr_15_7": "value_15_7_semantic_convention",
    "attr_15_8": "value_15_8_semantic_convention",
    "attr_15_9": "value_15_9_semantic_convention",
    "attr_15_10": "value_15_10_semantic_convention",
    "attr_15_11": "value_15_11_semantic_convention",
    "attr_15_12": "value_15_12_semantic_convention",
    "attr_15_13": "value_15_13_semantic_convention",
    "attr_15_14": "value_15_14_semantic_convention",
    "attr_15_15": "value_15_15_semantic_convention",
    "attr_15_16": "value_15_16_semantic_convention",
    "attr_15_17": "value_15_17_semantic_convention",
    "attr_15_18": "value_15_18_semantic_convention",
    "attr_15_19": "value_15_19_semantic_convention",
    "attr_15_20": "value_15_20_semantic_convention",
}


def apply_attrs_15(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_15.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_15() -> list[str]:
    return list(ATTRS_15.keys())
