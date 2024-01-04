#!/usr/bin/python3
""" Real definition of a rectangle Module """


class Rectangle:
    """ define Rectangle class """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with specified  width and height.

        Args:
           width: width of the rectangle default value 0.
           height: height of the rectangle default value 0.

        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ get width value """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the value of width.

        Args:
           value: the value to set on the width.
        Raises:
           TypeError: if width value not integer.
           ValueError: if width value less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ get height value """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height value

        Args:
           value: the value to set as height
        Raises:
           TypeError: if height value not integer.
           ValueError: if height value less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """ get the rectangle area """
        return self.__height * self.width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ''

        rectangle_str = ''
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str.rstrip('\n')

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ delete an instance of Rectangle """
        print("Bye rectangle...")
