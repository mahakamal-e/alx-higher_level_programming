#!/usr/bin/python3
""" Class Square """


class Square:
    """ Implementation of Square class """
    def __init__(self, size=0):
        """
        Initialization of square instance.

        Args:
            size: length of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
