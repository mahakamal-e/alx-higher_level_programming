#!/usr/bin/python3
""" Real definition of a rectangle Module """


class Rectangle:
    """ define Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with specified  width and height.

        Args:
           width: width of the rectangle default value 0.
           height: height of the rectangle default value 0.

        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return self.height * self.width

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ print the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ''

        rectangle_str = ''
        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + '\n'
        return rectangle_str.rstrip('\n')

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ delete an instance of Rectangle """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
