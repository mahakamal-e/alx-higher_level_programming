#!/usr/bin/python3
""" Base class Module """
import json
import os


class Base:
    """
    Implement of Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization for new instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
           cls: stands for "class" and is used to refer to the class itself.
           list_objs: a list of instances who inherits of Base
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file_:
            list_objs = [obj.to_dictionary() for obj in list_objs]
            file_.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ 
        Returns the list of the JSON string representation json_string.
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = None
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, "r", encoding="utf-8") as file_:
                 dict_list = cls.from_json_string(file_.read())
        instance_list = [cls.create(**dictionary) for dictionary in dict_list]
        return instance_list
