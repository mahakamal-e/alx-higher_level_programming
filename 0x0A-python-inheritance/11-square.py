#!/usr/bin/python3
""" Define Square Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Implement class Square """
    def __init__(self, size):
        """ Initialize a new instancle from Square class """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return the square description """
        return "[Square] {}/{}".format(self.__size, self.__size)
