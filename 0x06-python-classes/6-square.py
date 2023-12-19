#!/usr/bin/python3
"""creat a class Square."""


class Square:
    """ Define a Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a Square

        Args:
            size: length of the side of squre
            position: the position of Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Get the size of the new Square """
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size of the new Square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    @property
    def position(self):
        """a method used to retrieves the Square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """a method used to Set the Square position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """ get the current area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square in stdout with "#"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print('#' * self.__size)
