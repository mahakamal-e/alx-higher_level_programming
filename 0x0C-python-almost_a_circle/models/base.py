#!/usr/bin/python3
""" Base class Module """


class Base:
    """
    Implement of Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization for new instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
