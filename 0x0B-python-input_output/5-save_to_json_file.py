#!/usr/bin/python3
""" save_to_json_file Module """
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file
    using a JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as file_:
        json.dump(my_obj, file_)
