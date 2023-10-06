#!/usr/bin/env python3
"""Complex types annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiply float by multiplier"""
    
    def mul(n: float) -> float:
        """Multiply my multiplier"""
        return float(n * multiplier)
    return mul
