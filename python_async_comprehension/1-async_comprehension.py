#!/usr/bin/env python3
"""
This module provides a coroutine that collects values
using an asynchronous comprehension.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator and returns the list of random numbers.
    """
    return [i async for i in async_generator()]
