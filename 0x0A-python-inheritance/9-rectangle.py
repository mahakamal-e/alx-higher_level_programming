#!/usr/bin/python3
""" Define Rectangle Module """


class Rectangle(BaseGeometry):
    """Implement class Rectangle """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self._width = width
        self.integer_validator('height', height)
        self.__height = height
