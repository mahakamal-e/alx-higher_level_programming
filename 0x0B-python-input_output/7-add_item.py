#!/usr/bin/python3
""" 7-add_item Module """
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"


if __name__ == '__main__':
    filename = "add_item.json"
    python_list = sys.argv[1:]
    if os.path.exists(filename):
        python_list = load_from_json_file(filename) + python_list
    save_to_json_file(python_list, filename)
