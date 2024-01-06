#!/usr/bin/python3
""" locked class module """


class LockedClass:
    """ define LockedClass """
    def __setattr__(self, name, value):
        """ definr method setter called whenever
        an attribute is set on an object """
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
