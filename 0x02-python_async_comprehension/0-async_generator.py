#!/usr/bin/env python3
"""Async generator"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronous generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
