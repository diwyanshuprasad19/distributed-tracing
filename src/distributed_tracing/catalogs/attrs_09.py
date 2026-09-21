"""Semantic attribute catalog slice 09 for consistent span tagging."""

from __future__ import annotations

ATTRS_09: dict[str, str] = {
    "attr_9_1": "value_9_1_semantic_convention",
    "attr_9_2": "value_9_2_semantic_convention",
    "attr_9_3": "value_9_3_semantic_convention",
    "attr_9_4": "value_9_4_semantic_convention",
    "attr_9_5": "value_9_5_semantic_convention",
    "attr_9_6": "value_9_6_semantic_convention",
    "attr_9_7": "value_9_7_semantic_convention",
    "attr_9_8": "value_9_8_semantic_convention",
    "attr_9_9": "value_9_9_semantic_convention",
    "attr_9_10": "value_9_10_semantic_convention",
    "attr_9_11": "value_9_11_semantic_convention",
    "attr_9_12": "value_9_12_semantic_convention",
    "attr_9_13": "value_9_13_semantic_convention",
    "attr_9_14": "value_9_14_semantic_convention",
    "attr_9_15": "value_9_15_semantic_convention",
    "attr_9_16": "value_9_16_semantic_convention",
    "attr_9_17": "value_9_17_semantic_convention",
    "attr_9_18": "value_9_18_semantic_convention",
    "attr_9_19": "value_9_19_semantic_convention",
    "attr_9_20": "value_9_20_semantic_convention"
}


def apply_attrs_09(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_09.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_09() -> list[str]:
    return list(ATTRS_09.keys())
