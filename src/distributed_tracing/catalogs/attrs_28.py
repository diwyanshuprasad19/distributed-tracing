"""Semantic attribute catalog slice 28 for consistent span tagging."""

from __future__ import annotations

ATTRS_28: dict[str, str] = {
    "attr_28_1": "value_28_1_semantic_convention",
    "attr_28_2": "value_28_2_semantic_convention",
    "attr_28_3": "value_28_3_semantic_convention",
    "attr_28_4": "value_28_4_semantic_convention",
    "attr_28_5": "value_28_5_semantic_convention",
    "attr_28_6": "value_28_6_semantic_convention",
    "attr_28_7": "value_28_7_semantic_convention",
    "attr_28_8": "value_28_8_semantic_convention",
    "attr_28_9": "value_28_9_semantic_convention",
    "attr_28_10": "value_28_10_semantic_convention",
    "attr_28_11": "value_28_11_semantic_convention",
    "attr_28_12": "value_28_12_semantic_convention",
    "attr_28_13": "value_28_13_semantic_convention",
    "attr_28_14": "value_28_14_semantic_convention",
    "attr_28_15": "value_28_15_semantic_convention",
    "attr_28_16": "value_28_16_semantic_convention",
    "attr_28_17": "value_28_17_semantic_convention",
    "attr_28_18": "value_28_18_semantic_convention",
    "attr_28_19": "value_28_19_semantic_convention",
    "attr_28_20": "value_28_20_semantic_convention"
}


def apply_attrs_28(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_28.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_28() -> list[str]:
    return list(ATTRS_28.keys())
