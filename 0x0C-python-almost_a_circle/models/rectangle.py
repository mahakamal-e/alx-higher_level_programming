#!/usr/bin/python3
""" Define Rectangle Class """
from models.base import Base


class Rectangle(Base):
    """ Implementation of Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization for new instance "Constructor"

        Args:
           width: width
           height: height
           id: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the x value """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the y value """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the y value """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area """
        return self.width * self.height

    def display(self):
        """ display # rectangle """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """return a string representation of an object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}"\
            f"- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Method that returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "heigth": self.height, "x": self.x, "y": self.y}
