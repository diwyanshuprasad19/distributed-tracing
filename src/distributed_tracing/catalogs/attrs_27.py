"""Semantic attribute catalog slice 27 for consistent span tagging."""

from __future__ import annotations

ATTRS_27: dict[str, str] = {
    "attr_27_1": "value_27_1_semantic_convention",
    "attr_27_2": "value_27_2_semantic_convention",
    "attr_27_3": "value_27_3_semantic_convention",
    "attr_27_4": "value_27_4_semantic_convention",
    "attr_27_5": "value_27_5_semantic_convention",
    "attr_27_6": "value_27_6_semantic_convention",
    "attr_27_7": "value_27_7_semantic_convention",
    "attr_27_8": "value_27_8_semantic_convention",
    "attr_27_9": "value_27_9_semantic_convention",
    "attr_27_10": "value_27_10_semantic_convention",
    "attr_27_11": "value_27_11_semantic_convention",
    "attr_27_12": "value_27_12_semantic_convention",
    "attr_27_13": "value_27_13_semantic_convention",
    "attr_27_14": "value_27_14_semantic_convention",
    "attr_27_15": "value_27_15_semantic_convention",
    "attr_27_16": "value_27_16_semantic_convention",
    "attr_27_17": "value_27_17_semantic_convention",
    "attr_27_18": "value_27_18_semantic_convention",
    "attr_27_19": "value_27_19_semantic_convention",
    "attr_27_20": "value_27_20_semantic_convention"
}


def apply_attrs_27(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_27.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_27() -> list[str]:
    return list(ATTRS_27.keys())
