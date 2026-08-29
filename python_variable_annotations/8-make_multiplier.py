#!/usr/bin/env python3
"""
This module provides a function that returns another function
for multiplying a float by a predefined multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates and returns a function that multiplies a given float
    by the specified multiplier.
    """
    def multiply(n: float) -> float:
        """Multiplies a float by the outer multiplier."""
        return n * multiplier

    return multiply
