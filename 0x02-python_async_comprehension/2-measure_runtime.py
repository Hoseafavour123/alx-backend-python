#!/usr/bin/env python3
"""Measure runtime for four parallel comprehensions"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run in parallel"""
    start = time()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    end = time()

    return (end - start)
