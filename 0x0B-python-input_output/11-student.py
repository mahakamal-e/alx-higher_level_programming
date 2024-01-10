#!/usr/bin/python3
""" Class Student Module """


class Student:
    """defines a student by"""
    def __init__(self, first_name, last_name, age):
        """ Initialize  new instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        try:
            for attr_ in attrs:
                if type(attr_) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = {}
        for key in attrs:
            if hasattr(self, key):
                my_dict[key] = getattr(self, key)
        return my_dict

    def reload_from_json(self, json):
        """eplaces all attributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
