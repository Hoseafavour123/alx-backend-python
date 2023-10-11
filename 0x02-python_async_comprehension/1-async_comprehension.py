#!/usr/bin/env python3
"""Async comprehensions"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async comprehensions"""
    rand_nums = [num async for num in async_generator()]

    return rand_nums
