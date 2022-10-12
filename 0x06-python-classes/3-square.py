#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""a module for a square class with private args

Example:
    This module is expected to have a Class with private args
    The said file imports it as follows:
    Square = __import__('3-square').Square

    The outcome expected looks like this

    $ ./3-main.py
    Area: 9
    'Square' object has no attribute 'size'
    'Square' object has no attribute '__size'
    Area: 25
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


    def area(self):
        """Calculate the area of asquare based on size

        Note:
            Checks for type and value are already done

        Returns:
            Square of the size
        """

        return self.__size ** 2
