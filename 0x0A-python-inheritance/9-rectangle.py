#!/usr/bin/python3
""" Define Rectangle Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implement class Rectangle """
    def __init__(self, width, height):
        """ Define the Constructor """
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """get the area of rectangle """
        return self._width * self._height

    def __str__(self):
        """Method that return rectangle description """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
