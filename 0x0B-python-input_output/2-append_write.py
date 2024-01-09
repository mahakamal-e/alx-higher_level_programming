#!/usr/bin/python3
""" append_write Module """


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file."""
    with open(filename, 'a', encoding='utf-8') as file_:
        return file_.write(text)
