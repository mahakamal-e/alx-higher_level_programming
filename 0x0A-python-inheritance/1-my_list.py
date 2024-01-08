#!/usr/bin/python3
""" define class module """


class MyList(list):
    """
    a class MyList that inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
