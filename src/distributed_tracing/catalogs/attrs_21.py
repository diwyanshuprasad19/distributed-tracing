"""Semantic attribute catalog slice 21 for consistent span tagging."""

from __future__ import annotations

ATTRS_21: dict[str, str] = {
    "attr_21_1": "value_21_1_semantic_convention",
    "attr_21_2": "value_21_2_semantic_convention",
    "attr_21_3": "value_21_3_semantic_convention",
    "attr_21_4": "value_21_4_semantic_convention",
    "attr_21_5": "value_21_5_semantic_convention",
    "attr_21_6": "value_21_6_semantic_convention",
    "attr_21_7": "value_21_7_semantic_convention",
    "attr_21_8": "value_21_8_semantic_convention",
    "attr_21_9": "value_21_9_semantic_convention",
    "attr_21_10": "value_21_10_semantic_convention",
    "attr_21_11": "value_21_11_semantic_convention",
    "attr_21_12": "value_21_12_semantic_convention",
    "attr_21_13": "value_21_13_semantic_convention",
    "attr_21_14": "value_21_14_semantic_convention",
    "attr_21_15": "value_21_15_semantic_convention",
    "attr_21_16": "value_21_16_semantic_convention",
    "attr_21_17": "value_21_17_semantic_convention",
    "attr_21_18": "value_21_18_semantic_convention",
    "attr_21_19": "value_21_19_semantic_convention",
    "attr_21_20": "value_21_20_semantic_convention",
}


def apply_attrs_21(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_21.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_21() -> list[str]:
    return list(ATTRS_21.keys())
