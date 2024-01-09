#!/usr/bin/python3
""" Define read_file Module """


def read_file(filename=""):
    """ Implement a function that reads a text file (UTF8)
    and prints it to stdout

    Args:
       filename: file name as input.
    """
    with open(filename, 'r', encoding='utf-8') as file_:
        print(file_.read(), end="")
