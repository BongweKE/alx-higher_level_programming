#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Module file for rectangle.py"""
from models.base import Base

class Rectangle(Base):
    """A child class of base to represent a mathematical rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for the rectangle instances
        It first calls the Base class to instanciate id then uses private
        attributes as explained below
        Attrs:
            width (int): The width of the rectangle
            height (int): mathematical height
            x (int): Location on the x axis of a 2d plane
            y (int): Location on the y axis of a 2d plane
        """

        name = "width"
        if type(width) != int:
            raise TypeError(f"{name} must be an integer")
        elif width <= 0:
            raise ValueError(f"{name} must be > 0")

        name = "height"
        if type(height) != int:
            raise TypeError(f"{name} must be an integer")
        elif height <= 0:
            raise ValueError(f"{name} must be > 0")

        name = "x"
        if type(x) != int:
            raise TypeError(f"{name} must be an integer")
        if x < 0:
            raise ValueError(f"{name} must be >= 0")


        name = "y"
        if type(y) != int:
            raise TypeError(f"{name} must be an integer")
        if y < 0:
            raise ValueError(f"{name} must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter class for width attribute"""
        return self.__width

    @width.setter
    def width(self, val):
        """Setter class for width attribute
        Attr:
            val: the value to be set as the width
        """
        name = "width"
        if type(val) != int:
            raise TypeError(f"{name} must be an integer")
        elif val <= 0:
            raise ValueError(f"{name} must be > 0")

        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        """Setter class for height attribute
        Attr:
            val: the value to be set as the height
        """
        name = "height"
        if type(height) != int:
            raise TypeError(f"{name} must be an integer")
        elif height <= 0:
            raise ValueError(f"{name} must be > 0")

        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        """Setter class for x attribute
        Attr:
            val: the value to be set as x
        """
        name = "x"
        if type(x) != int:
            raise TypeError(f"{name} must be an integer")
        if x < 0:
            raise ValueError(f"{name} must be >= 0")

        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        """Setter class for y attribute
        Attr:
            val: the value to be set as y
        """
        name = "y"
        if type(y) != int:
            raise TypeError(f"{name} must be an integer")
        if y < 0:
            raise ValueError(f"{name} must be >= 0")

        self.__y = val

    def area(self):
        """A method to calculate area of a reactangle"""
        return self.__width * self.__height

    def display(self):
        """A method to display a rectangle using #"""
        for a_y in range(self.__y):
            print()
        spaces = ''.join([' ' for i in range(self.__x)])
        for i in range(self.__height):
            print(spaces, end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """A method to define how the user sees the rectangle instance"""
        str1 = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        str2 = f"{self.__width}/{self.__height}"
        return f"{str1} - {str2}"

    def update(self, *args, **kwargs):
        """update id, width, height, x, y
        In that spacific order
        """
        if args is not None and len(args) != 0:
            try:
                if args[0] is not None:
                    self.id = args[0]
                if args[1] is not None:
                    self.__width = args[1]
                if args[2] is not None:
                    self.__height = args[2]
                if args[3] is not None:
                    self.__x = args[3]
                if args[4] is not None:
                    self.__y = args[4]
            except IndexError:
                pass
        elif kwargs is not None:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.__width = v
                if k == "height":
                    self.__height = v
                if k == "x":
                    self.__x = v
                if k == "y":
                    self.__y = v
