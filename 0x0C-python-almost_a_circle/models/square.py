#!/usr/bin/python3
""" Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Implement class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization Method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string info about class square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ get for the value size """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        args_length = len(args)
        if args_length != 0:
            if args_length >= 1:
                self.id = args[0]
            if args_length >= 2:
                self.width = args[1]
            if args_length >= 3:
                self.x = args[2]
            if args_length >= 4:
                self.y = args[3]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
