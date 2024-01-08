#!/usr/bin/python3
""" define function called inherits_from """


def inherits_from(obj, a_class):
    """
     function that returns True if the object is an instance
     otherwise returns False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
