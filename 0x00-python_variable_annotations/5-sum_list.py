#!/usr/bin/env python3
"""Complex Types"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums list"""
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
