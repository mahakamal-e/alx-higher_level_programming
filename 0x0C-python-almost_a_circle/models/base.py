#!/usr/bin/python3
""" Base class Module """
import json
import os
import csv


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
            return "[]"
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
            new_instance = cls(1, 1)
        else:
            new_instance = cls(1)
        new_instance.update(**dictionary)

        return new_instance

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as file_:
            if list_objs is None or list_objs == []:
                file_.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                                 for obj in list_objs]
                else:
                    list_objs = [[obj.id, obj.size, obj.x, obj.y]
                                 for obj in list_objs]
                csv_writer = csv.writer(file_)
                csv_writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        list_ = []
        with open(filename, "r", encoding="utf-8") as file_:
            csv_reader = csv.reader(file_)
            for i in csv_reader:
                i = [int(line) for line in i]
                if cls.__name__ == "Rectangle":
                    dict_ = {"id": i[0], "width": i[1], "height": i[2],
                             "x": i[3], "y": i[4]}
                else:
                    dict_ = {"id": i[0], "size": i[1],
                             "x": i[2], "y": i[3]}
                list_.append(cls.create(**dict_))
        return list_
