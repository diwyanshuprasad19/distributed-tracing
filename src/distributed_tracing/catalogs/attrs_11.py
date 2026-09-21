"""Semantic attribute catalog slice 11 for consistent span tagging."""

from __future__ import annotations

ATTRS_11: dict[str, str] = {
    "attr_11_1": "value_11_1_semantic_convention",
    "attr_11_2": "value_11_2_semantic_convention",
    "attr_11_3": "value_11_3_semantic_convention",
    "attr_11_4": "value_11_4_semantic_convention",
    "attr_11_5": "value_11_5_semantic_convention",
    "attr_11_6": "value_11_6_semantic_convention",
    "attr_11_7": "value_11_7_semantic_convention",
    "attr_11_8": "value_11_8_semantic_convention",
    "attr_11_9": "value_11_9_semantic_convention",
    "attr_11_10": "value_11_10_semantic_convention",
    "attr_11_11": "value_11_11_semantic_convention",
    "attr_11_12": "value_11_12_semantic_convention",
    "attr_11_13": "value_11_13_semantic_convention",
    "attr_11_14": "value_11_14_semantic_convention",
    "attr_11_15": "value_11_15_semantic_convention",
    "attr_11_16": "value_11_16_semantic_convention",
    "attr_11_17": "value_11_17_semantic_convention",
    "attr_11_18": "value_11_18_semantic_convention",
    "attr_11_19": "value_11_19_semantic_convention",
    "attr_11_20": "value_11_20_semantic_convention",
}


def apply_attrs_11(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_11.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_11() -> list[str]:
    return list(ATTRS_11.keys())
