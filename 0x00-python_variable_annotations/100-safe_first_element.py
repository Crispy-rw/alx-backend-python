#!/usr/bin/env python3
"""
Contains type-annotated function
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Type-annotated function"""
    if lst:
        return lst[0]
    else:
        return None
