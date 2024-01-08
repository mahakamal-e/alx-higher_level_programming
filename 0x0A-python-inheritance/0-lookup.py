#!/usr/bin/python3
""" Define function called lookup """


def lookup(obj):
    """ Looked up available attributes and methods of an object
    Args:
       obj: object of the list
    Return:
         list of the attributes
    """
    return dir(obj)
