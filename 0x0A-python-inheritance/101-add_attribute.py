#!/usr/bin/python3
""" function module """


def add_attribute(obj, attribute_name, value):
    """adds a new attribute to an object if it’s possible
    Args:
       obj: object name as input.
       attribute_name: attribute name to store data in.
       value: data that stored in the attribute.
    Raises:
       TypeError: If the object can't have new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attribute_name, value)
