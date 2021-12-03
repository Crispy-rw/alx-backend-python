#!/usr/bin/env python3
"""
Contains a type-annotated function that takes in a float and returns its floor
"""
import math


def floor(n: float) -> int:
    """
    Returns the floor of the float it takes in as an argument
    Argument:
        n (float): number to return float of
    Return: int
    """
    return math.floor(n)
