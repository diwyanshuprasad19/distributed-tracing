"""Semantic attribute catalog slice 10 for consistent span tagging."""

from __future__ import annotations

ATTRS_10: dict[str, str] = {
    "attr_10_1": "value_10_1_semantic_convention",
    "attr_10_2": "value_10_2_semantic_convention",
    "attr_10_3": "value_10_3_semantic_convention",
    "attr_10_4": "value_10_4_semantic_convention",
    "attr_10_5": "value_10_5_semantic_convention",
    "attr_10_6": "value_10_6_semantic_convention",
    "attr_10_7": "value_10_7_semantic_convention",
    "attr_10_8": "value_10_8_semantic_convention",
    "attr_10_9": "value_10_9_semantic_convention",
    "attr_10_10": "value_10_10_semantic_convention",
    "attr_10_11": "value_10_11_semantic_convention",
    "attr_10_12": "value_10_12_semantic_convention",
    "attr_10_13": "value_10_13_semantic_convention",
    "attr_10_14": "value_10_14_semantic_convention",
    "attr_10_15": "value_10_15_semantic_convention",
    "attr_10_16": "value_10_16_semantic_convention",
    "attr_10_17": "value_10_17_semantic_convention",
    "attr_10_18": "value_10_18_semantic_convention",
    "attr_10_19": "value_10_19_semantic_convention",
    "attr_10_20": "value_10_20_semantic_convention"
}


def apply_attrs_10(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_10.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_10() -> list[str]:
    return list(ATTRS_10.keys())
