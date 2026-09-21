"""Semantic attribute catalog slice 08 for consistent span tagging."""

from __future__ import annotations

ATTRS_08: dict[str, str] = {
    "attr_8_1": "value_8_1_semantic_convention",
    "attr_8_2": "value_8_2_semantic_convention",
    "attr_8_3": "value_8_3_semantic_convention",
    "attr_8_4": "value_8_4_semantic_convention",
    "attr_8_5": "value_8_5_semantic_convention",
    "attr_8_6": "value_8_6_semantic_convention",
    "attr_8_7": "value_8_7_semantic_convention",
    "attr_8_8": "value_8_8_semantic_convention",
    "attr_8_9": "value_8_9_semantic_convention",
    "attr_8_10": "value_8_10_semantic_convention",
    "attr_8_11": "value_8_11_semantic_convention",
    "attr_8_12": "value_8_12_semantic_convention",
    "attr_8_13": "value_8_13_semantic_convention",
    "attr_8_14": "value_8_14_semantic_convention",
    "attr_8_15": "value_8_15_semantic_convention",
    "attr_8_16": "value_8_16_semantic_convention",
    "attr_8_17": "value_8_17_semantic_convention",
    "attr_8_18": "value_8_18_semantic_convention",
    "attr_8_19": "value_8_19_semantic_convention",
    "attr_8_20": "value_8_20_semantic_convention",
}


def apply_attrs_08(span, prefix: str = "custom") -> None:
    for k, v in ATTRS_08.items():
        span.set_attribute(f"{prefix}.{k}", v)


def keys_08() -> list[str]:
    return list(ATTRS_08.keys())
