#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A method to implement instances of Squares"""

    def __init__(self, size):
        """A method to initialize the super with correct values"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """A method to facilitate how it's printed to the users"""
        return f"[Square] {self.__size}/{self.__size}"
