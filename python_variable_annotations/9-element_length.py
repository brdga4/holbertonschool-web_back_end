#!/usr/bin/env python3
"""
This module provides a duck-typed function that calculates
the lengths of elements in an iterable collection.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing an element and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
