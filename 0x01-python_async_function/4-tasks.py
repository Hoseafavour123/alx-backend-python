#!/usr/bin/env python3
"""Concurrent coroutines"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with max_delay"""
    my_tasks = [task_wait_random(max_delay) for i in range(n)]
    my_delays = [await task for task in asyncio.as_completed(my_tasks)]
    return my_delays
