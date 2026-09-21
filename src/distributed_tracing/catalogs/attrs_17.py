"""Semantic attribute catalog slice 17 for consistent span tagging."""

from __future__ import annotations

ATTRS_17: dict[str, str] = {
    "attr_17_1": "value_17_1_semantic_convention",
    "attr_17_2": "value_17_2_semantic_convention",
    "attr_17_3": "value_17_3_semantic_convention",
    "attr_17_4": "value_17_4_semantic_convention",
    "attr_17_5": "value_17_5_semantic_convention",
    "attr_17_6": "value_17_6_semantic_convention",
    "attr_17_7": "value_17_7_semantic_convention",
    "attr_17_8": "value_17_8_semantic_convention",
    "attr_17_9": "value_17_9_semantic_convention",
    "attr_17_10": "value_17_10_semantic_convention",
    "attr_17_11": "value_17_11_semantic_convention",
    "attr_17_12": "value_17_12_semantic_convention",
    "attr_17_13": "value_17_13_semantic_convention",
    "attr_17_14": "value_17_14_semantic_convention",
    "attr_17_15": "value_17_15_semantic_convention",
    "attr_17_16": "value_17_16_semantic_convention",
    "attr_17_17": "value_17_17_semantic_convention",
    "attr_17_18": "value_17_18_semantic_convention",
    "attr_17_19": "value_17_19_semantic_convention",
    "attr_17_20": "value_17_20_semantic_convention",
}


def apply_attrs_17(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_17.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_17() -> list[str]:
    return list(ATTRS_17.keys())
