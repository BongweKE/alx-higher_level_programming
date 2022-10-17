#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A module containing definition of a real rectangle

Note:
    It can calculate Area and Perimeter
"""


class Rectangle:
    """A realistic mathematical rectangle"""

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

    def area(self):
        """A method to calculate rectangle area

        Return: height * width
        """
        return self.__height * self.width

    def perimeter(self):
        """A method to calculate perimeter

        Note:
            If height or width is zero perimeter is 0
        Return: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__height * 2) + (self.width * 2)

    def __str__(self):
        """A method to define how to define the rectangle
        Note:
            It's going to be represented using #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        nl = "\n"
        pr_rec = nl.join(
            [''.join(['#' for i in range(self.__width)])
             for i in range(self.__height)])
        return f"{pr_rec}"

    def __repr__(self):
        """method to return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width},{self.__height})"
