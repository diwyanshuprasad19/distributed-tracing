"""Semantic attribute catalog slice 30 for consistent span tagging."""

from __future__ import annotations

ATTRS_30: dict[str, str] = {
    "attr_30_1": "value_30_1_semantic_convention",
    "attr_30_2": "value_30_2_semantic_convention",
    "attr_30_3": "value_30_3_semantic_convention",
    "attr_30_4": "value_30_4_semantic_convention",
    "attr_30_5": "value_30_5_semantic_convention",
    "attr_30_6": "value_30_6_semantic_convention",
    "attr_30_7": "value_30_7_semantic_convention",
    "attr_30_8": "value_30_8_semantic_convention",
    "attr_30_9": "value_30_9_semantic_convention",
    "attr_30_10": "value_30_10_semantic_convention",
    "attr_30_11": "value_30_11_semantic_convention",
    "attr_30_12": "value_30_12_semantic_convention",
    "attr_30_13": "value_30_13_semantic_convention",
    "attr_30_14": "value_30_14_semantic_convention",
    "attr_30_15": "value_30_15_semantic_convention",
    "attr_30_16": "value_30_16_semantic_convention",
    "attr_30_17": "value_30_17_semantic_convention",
    "attr_30_18": "value_30_18_semantic_convention",
    "attr_30_19": "value_30_19_semantic_convention",
    "attr_30_20": "value_30_20_semantic_convention"
}


def apply_attrs_30(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_30.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_30() -> list[str]:
    return list(ATTRS_30.keys())
