#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module for class BaseGeometry() which validates integers"""


class BaseGeometry:
    """A class To perform basic geometry"""
    def __init__(self):
        """ a method to initialize the class instance"""
        pass

    def area(self):
        """ a method to calculate area of a geometrical figure"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a method to validate values for the BaseGeometry instance"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
