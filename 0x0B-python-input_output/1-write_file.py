#!/usr/bin/python3
""" write_file Module """


def write_file(filename="", text=""):
    """ Define a function that writes a string to a text file"""
    with open(filename, 'w', encoding='utf-8') as file_:
        return file_.write(text)
