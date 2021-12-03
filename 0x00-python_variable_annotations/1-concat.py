#!/usr/bin/env python3
"""
Contains type-annotated function that takes in two strings and
concatenates them.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.
    Arguments:
        str1 (str): first string
        str2 (str): second string
    Return type: string
    """
    return "{}{}".format(str1, str2)
