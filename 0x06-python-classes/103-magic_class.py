#!/usr/bin/python3
""" Class MagicClass """

import math


class MagicClass:
    """ Define a MagicClass """

    def __init__(self, radius=0):
        """
        init

        Args:
            radius: the redius
        """
        self.__radius = 0
        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ method that returns the area """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """ method that returns circumference """
        return (2 * math.pi * self.__radius)
