#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A method to implement instances of Squares"""

    def __init__(self, size):
        """A method to initialize an instance of Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
