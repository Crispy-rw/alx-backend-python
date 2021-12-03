#!/usr/bin/env python3
"""
Contains a type-annotated function
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a tuple composed of a list element and the length of
       the list
    """
    return [(i, len(i)) for i in lst]
