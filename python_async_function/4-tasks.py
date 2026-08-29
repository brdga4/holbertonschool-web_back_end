#!/usr/bin/env python3
"""
This module provides a function that executes multiple tasks
concurrently and returns their results in ascending order.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort().
    """
    # Create a list of n Tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    # as_completed yields tasks as they finish. 
    # Since the delay time is what the task waits for, 
    # the ones that wait the least finish first.
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
