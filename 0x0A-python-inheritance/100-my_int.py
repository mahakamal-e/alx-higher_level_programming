#!/usr/bin/python3
""" Define module MyInt """


class MyInt(int):
    """ Implement class MyInt """
    def __eq__(self, other):
        """ reverse == operator """
        return not super().__eq__(other)
    def __ne__(self, other):
        """ reverse != operator """
        return not super().__ne__(other)
