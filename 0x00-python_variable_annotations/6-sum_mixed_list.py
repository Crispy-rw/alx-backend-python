#!/usr/bin/env python3
"""
Contains type-annotated function which takes a list of integers
and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats and integers
    Arguments:
        mxd_lst (list): list of floats and integers
    Return: float
    """
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
