"""Semantic attribute catalog slice 20 for consistent span tagging."""

from __future__ import annotations

ATTRS_20: dict[str, str] = {
    "attr_20_1": "value_20_1_semantic_convention",
    "attr_20_2": "value_20_2_semantic_convention",
    "attr_20_3": "value_20_3_semantic_convention",
    "attr_20_4": "value_20_4_semantic_convention",
    "attr_20_5": "value_20_5_semantic_convention",
    "attr_20_6": "value_20_6_semantic_convention",
    "attr_20_7": "value_20_7_semantic_convention",
    "attr_20_8": "value_20_8_semantic_convention",
    "attr_20_9": "value_20_9_semantic_convention",
    "attr_20_10": "value_20_10_semantic_convention",
    "attr_20_11": "value_20_11_semantic_convention",
    "attr_20_12": "value_20_12_semantic_convention",
    "attr_20_13": "value_20_13_semantic_convention",
    "attr_20_14": "value_20_14_semantic_convention",
    "attr_20_15": "value_20_15_semantic_convention",
    "attr_20_16": "value_20_16_semantic_convention",
    "attr_20_17": "value_20_17_semantic_convention",
    "attr_20_18": "value_20_18_semantic_convention",
    "attr_20_19": "value_20_19_semantic_convention",
    "attr_20_20": "value_20_20_semantic_convention",
}


def apply_attrs_20(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_20.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_20() -> list[str]:
    return list(ATTRS_20.keys())
