#!/usr/bin/env python3
"""Type-annotated function"""
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """Type-annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
