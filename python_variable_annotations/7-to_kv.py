#!/usr/bin/env python3
"""
This module provides a function that returns a tuple containing
a string key and the square of a numeric value.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v, and returns a tuple
    with k and the square of v (as a float).
    """
    return (k, v ** 2)
