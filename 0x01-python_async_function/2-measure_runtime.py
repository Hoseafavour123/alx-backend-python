#!/usr/bin/env python3
"""Measure the run time"""
import asyncio
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure execution time"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()

    return (end - start) / n
