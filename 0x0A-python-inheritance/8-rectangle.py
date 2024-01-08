#!/usr/bin/python3
""" Define Rectangle Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implement class Rectangle """

    def __init__(self, width, height):
        """ Initialization Method
        Args:
           width: instance width
           height: istance height
        """
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self.__height = height
