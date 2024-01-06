#!/usr/bin/python3
""" locked class module """


class LockedClass:
    """ define LockedClass """
    def __setattr__(self, name, value):
        """ definr method setter called whenever
        an attribute is set on an object """

        __slots__ = "first_name"
