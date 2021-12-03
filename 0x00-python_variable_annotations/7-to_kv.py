#!/usr/bin/env python3
"""
Contains type-annotated functiono that takes a string and an
int or float and returns a tuple containing a string and
the square of the float/int
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes in a string and a number (float/int) and returns a tuple
    containing the string and the square of the number as a float
    Arguments:
        k (str): string
        v (int or float): number
    Return: Tuple[string, float]
    """
    return (k, v * v)
