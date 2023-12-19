#!/usr/bin/python3
""" Class Square """


class Square:
    """ Implementation of Square class """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of square instance.

        Args:
            size: length of the square.
            position: define the position of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ property used to retrieve position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ method used to set the data of position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method returns the current area """

        return self.__size * self.__size

    def my_print(self):
        """ method that prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
