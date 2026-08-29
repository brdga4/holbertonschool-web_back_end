#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits
for a random amount of time and returns the delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive)
    seconds and returns the length of the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
