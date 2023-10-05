#!/usr/bin/env python3
from typing import Union, Tuple
"""Complex Types"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """string and int/float to tuple"""
    int_float: float = v ** 2
    return (k, int_float)
