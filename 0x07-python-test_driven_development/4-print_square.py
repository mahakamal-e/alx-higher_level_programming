#!/usr/bin/python3
""" print_square module """


def print_square(size):
    """ a function that prints a square with the character #.

    Args:
       size: is the size length of the square.

    Raises:
        TypeError: if size not integer
            or if size is a float and is less than 0.
        ValueError: if size less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
