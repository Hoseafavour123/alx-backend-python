#!/usr/bin/env python3
"""Complex Types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of list"""
    return float(sum(mxd_lst))
