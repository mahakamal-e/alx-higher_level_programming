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
        self.__size = size

    @property
    def size(self):
        """property used to getter (get the length of square)"""
        return self.__size

    @size.setter
    def size(self, value):
        """ method usued to set the data of size """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ Method returns the current area """

        return self.__size * self.__size

    def my_print(self):
        """ method that prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                # This loop iterates self.__size times
                # creating each row of the square.
                print("#" * self.__size)
