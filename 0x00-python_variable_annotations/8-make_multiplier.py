#!/usr/bin/env python3
"""
Contains a type-annotated function that takes a float and returns a function
that multiplies a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float and returns a function that multiplies a float by the float
    Argument:
        multiplier (float): number to be multiplied
    Return: function that multiplies multiplier by a float
    """
    def x(y: float) -> float:
        return y * multiplier
    return x
