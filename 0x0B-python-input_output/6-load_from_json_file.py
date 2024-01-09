#!/usr/bin/python3
""" load_from_json_file Module """
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a “JSON file” """
    with open(filename, 'w', encoding='utf-8') as as file_:
        return json.load(file_)
