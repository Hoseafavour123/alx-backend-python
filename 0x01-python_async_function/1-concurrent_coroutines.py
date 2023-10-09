#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay"""
    my_tasks = [asyncio.create_task(wait_random()) for i in range(n)]
    my_delays = [await task for task in asyncio.as_completed(my_tasks)]
    return my_delays
