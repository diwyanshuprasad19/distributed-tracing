"""Semantic attribute catalog slice 26 for consistent span tagging."""

from __future__ import annotations

ATTRS_26: dict[str, str] = {
    "attr_26_1": "value_26_1_semantic_convention",
    "attr_26_2": "value_26_2_semantic_convention",
    "attr_26_3": "value_26_3_semantic_convention",
    "attr_26_4": "value_26_4_semantic_convention",
    "attr_26_5": "value_26_5_semantic_convention",
    "attr_26_6": "value_26_6_semantic_convention",
    "attr_26_7": "value_26_7_semantic_convention",
    "attr_26_8": "value_26_8_semantic_convention",
    "attr_26_9": "value_26_9_semantic_convention",
    "attr_26_10": "value_26_10_semantic_convention",
    "attr_26_11": "value_26_11_semantic_convention",
    "attr_26_12": "value_26_12_semantic_convention",
    "attr_26_13": "value_26_13_semantic_convention",
    "attr_26_14": "value_26_14_semantic_convention",
    "attr_26_15": "value_26_15_semantic_convention",
    "attr_26_16": "value_26_16_semantic_convention",
    "attr_26_17": "value_26_17_semantic_convention",
    "attr_26_18": "value_26_18_semantic_convention",
    "attr_26_19": "value_26_19_semantic_convention",
    "attr_26_20": "value_26_20_semantic_convention"
}


def apply_attrs_26(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_26.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_26() -> list[str]:
    return list(ATTRS_26.keys())
