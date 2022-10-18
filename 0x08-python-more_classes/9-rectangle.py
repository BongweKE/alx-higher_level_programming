#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" A module containing definition of a real rectangle

Note:
    It can calculate Area and Perimeter
"""


class Rectangle:
    """A realistic mathematical rectangle

    Attrs:
        number_of_instances (int):Public class attribute
            Initialized to 0
            Incremented during each new instance instantiation
            Decremented during each instance deletion
        print_symbol (str, any type): Public class attribute
            Initialized to #
            Used as symbol for string representation
            Can be any type
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method to initialize the Rectangle
        Attrs:
            width (int): The width of the rectangle
            height (int): The rectangle height

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            [''.join([Rectangle.print_symbol for i in range(self.__width)])
             for i in range(self.__height)])
        return f"{pr_rec}"

    def __repr__(self):
        """method to return a string representation of the rectangle to be
        able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        """method to Print the message Bye rectangle...
        (... being 3 dots not ellipsis) when an instance
        of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle based on the area

        Checks:
            rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message
        
        rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message
        
        Returns rect_1 if both have the same area value

        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area()\
           or rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        """Class method  that returns a new
        Rectangle instance with width == height == size
        """
        return Rectangle(size,size)
