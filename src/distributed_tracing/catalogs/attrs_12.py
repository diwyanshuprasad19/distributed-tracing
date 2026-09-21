"""Semantic attribute catalog slice 12 for consistent span tagging."""

from __future__ import annotations

ATTRS_12: dict[str, str] = {
    "attr_12_1": "value_12_1_semantic_convention",
    "attr_12_2": "value_12_2_semantic_convention",
    "attr_12_3": "value_12_3_semantic_convention",
    "attr_12_4": "value_12_4_semantic_convention",
    "attr_12_5": "value_12_5_semantic_convention",
    "attr_12_6": "value_12_6_semantic_convention",
    "attr_12_7": "value_12_7_semantic_convention",
    "attr_12_8": "value_12_8_semantic_convention",
    "attr_12_9": "value_12_9_semantic_convention",
    "attr_12_10": "value_12_10_semantic_convention",
    "attr_12_11": "value_12_11_semantic_convention",
    "attr_12_12": "value_12_12_semantic_convention",
    "attr_12_13": "value_12_13_semantic_convention",
    "attr_12_14": "value_12_14_semantic_convention",
    "attr_12_15": "value_12_15_semantic_convention",
    "attr_12_16": "value_12_16_semantic_convention",
    "attr_12_17": "value_12_17_semantic_convention",
    "attr_12_18": "value_12_18_semantic_convention",
    "attr_12_19": "value_12_19_semantic_convention",
    "attr_12_20": "value_12_20_semantic_convention"
}


def apply_attrs_12(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_12.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_12() -> list[str]:
    return list(ATTRS_12.keys())
