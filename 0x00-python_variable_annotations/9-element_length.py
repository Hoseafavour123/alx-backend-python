#!/usr/bin/env python3
from typing import Sequence, List, Tuple, Iterable
"""Duck typing annotations"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Lets duck annotations"""
    return [(i, len(i)) for i in lst]
