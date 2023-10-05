#!/usr/bin/env python3
from typing import Sequence, List, Tuple, Iterable
"""Duck typing"""

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Lets duck"""
    return [(i, len(i)) for i in lst]
