#!/usr/bin/env python3
"""
Contains a type-annotated function that takes a list of floats
and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of floats passed in as a list
    Arguments:
        input_list (float): list of floats
    Return: float
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
