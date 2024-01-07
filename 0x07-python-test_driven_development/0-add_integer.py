#!/usr/bin/python3
"""
Defineadd integer module
"""


def add_integer(a, b=98):
    """a function that adds 2 integers
    Args:
       a: int or float number
       b: int or float number
    """

    if a is None or not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if b is None or not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
