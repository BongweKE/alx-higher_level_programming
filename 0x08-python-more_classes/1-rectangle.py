#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A module containing definition of a real rectangle """


class Rectangle:
    """A realistic mathematical rectangle

    Attrs:
        __width (int): width
        __height (int): height

    """

    def __init__(self, width=0, height=0):
        """Method to initialize the Rectangle
        Attrs:
            width (int): The width of the rectangle
            height (int): The rectangle height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: the width of our rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        else:
            self.__width = value

    @property
    def height(self):
        """int: the height of our rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        else:
            self.__height = value
