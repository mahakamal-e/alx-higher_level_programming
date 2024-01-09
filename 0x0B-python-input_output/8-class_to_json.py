#!/usr/bin/python3
""" class_to_json Module """


def class_to_json(obj):
    """ define function that returns the dictionary description"""
    return obj.__dict__
