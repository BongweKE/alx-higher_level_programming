#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Module file for square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class to define Square mathematical representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializer method for square instances
        Attrs:
            width (int): The width of the rectangle
            height (int): mathematical height
            x (int): Location on the x axis of a 2d plane
            y (int): Location on the y axis of a 2d plane
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """A method to define how the user sees the square instance"""
        str1 = f"[Square] ({self.id}) {self.x}/{self.y}"
        str2 = f"{self.size}"
        return f"{str1} - {str2}"

    @property
    def size(self):
        """Getter class for size attribute"""
        return self.width

    @size.setter
    def size(self, val):
        """Setter class for size attribute
        Attr:
            width: size setter for width
        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """update id, size, x, y
        In that spacific order
        """
        if args is not None and len(args) != 0:
            try:
                if args[0] is not None:
                    setattr(self, 'id', args[0])
                if args[1] is not None:
                    self.size = args[1]
                if args[2] is not None:
                    self.x = args[2]
                if args[3] is not None:
                    setattr(self, 'y', args[3])
            except IndexError:
                pass
        elif kwargs is not None:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """Method to present a Square as a dictionary"""
        return {
            'id': self.id,
            'x': self.x,
            'y': self.y,
            'size': self.size
        }
