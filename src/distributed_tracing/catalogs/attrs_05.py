"""Semantic attribute catalog slice 05 for consistent span tagging."""

from __future__ import annotations

ATTRS_05: dict[str, str] = {
    "attr_5_1": "value_5_1_semantic_convention",
    "attr_5_2": "value_5_2_semantic_convention",
    "attr_5_3": "value_5_3_semantic_convention",
    "attr_5_4": "value_5_4_semantic_convention",
    "attr_5_5": "value_5_5_semantic_convention",
    "attr_5_6": "value_5_6_semantic_convention",
    "attr_5_7": "value_5_7_semantic_convention",
    "attr_5_8": "value_5_8_semantic_convention",
    "attr_5_9": "value_5_9_semantic_convention",
    "attr_5_10": "value_5_10_semantic_convention",
    "attr_5_11": "value_5_11_semantic_convention",
    "attr_5_12": "value_5_12_semantic_convention",
    "attr_5_13": "value_5_13_semantic_convention",
    "attr_5_14": "value_5_14_semantic_convention",
    "attr_5_15": "value_5_15_semantic_convention",
    "attr_5_16": "value_5_16_semantic_convention",
    "attr_5_17": "value_5_17_semantic_convention",
    "attr_5_18": "value_5_18_semantic_convention",
    "attr_5_19": "value_5_19_semantic_convention",
    "attr_5_20": "value_5_20_semantic_convention",
}


def apply_attrs_05(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_05.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_05() -> list[str]:
    return list(ATTRS_05.keys())
