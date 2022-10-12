#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""a module for a square class with private args

Example:
    This module is expected to have a Class with private args
    $ ./2-main.py
    <class '2-square.Square'>
    {'_Square__size': 3}
    <class '2-square.Square'>
    {'_Square__size': 0}
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'
    size must be an integer
    size must be >= 0
"""
class Square:
    """a class Square that defines a mathematical square
    """
    def __init__(self, size=0):
        """Initialization of Class Square

        Args:
            __size (int): length or width should be equal and private
        Note:
            size is expected to be an integer >= 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
