"""Semantic attribute catalog slice 19 for consistent span tagging."""

from __future__ import annotations

ATTRS_19: dict[str, str] = {
    "attr_19_1": "value_19_1_semantic_convention",
    "attr_19_2": "value_19_2_semantic_convention",
    "attr_19_3": "value_19_3_semantic_convention",
    "attr_19_4": "value_19_4_semantic_convention",
    "attr_19_5": "value_19_5_semantic_convention",
    "attr_19_6": "value_19_6_semantic_convention",
    "attr_19_7": "value_19_7_semantic_convention",
    "attr_19_8": "value_19_8_semantic_convention",
    "attr_19_9": "value_19_9_semantic_convention",
    "attr_19_10": "value_19_10_semantic_convention",
    "attr_19_11": "value_19_11_semantic_convention",
    "attr_19_12": "value_19_12_semantic_convention",
    "attr_19_13": "value_19_13_semantic_convention",
    "attr_19_14": "value_19_14_semantic_convention",
    "attr_19_15": "value_19_15_semantic_convention",
    "attr_19_16": "value_19_16_semantic_convention",
    "attr_19_17": "value_19_17_semantic_convention",
    "attr_19_18": "value_19_18_semantic_convention",
    "attr_19_19": "value_19_19_semantic_convention",
    "attr_19_20": "value_19_20_semantic_convention"
}


def apply_attrs_19(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_19.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_19() -> list[str]:
    return list(ATTRS_19.keys())
