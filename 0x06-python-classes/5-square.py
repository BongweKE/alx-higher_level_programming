#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""a module for a square class with private args that can calculate area

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

    $ ./4-main.py
    Area: 7921 for size: 89
    Area: 9 for size: 3
    size must be an integer
    $

    $ ./5-main.py
    ###
    ###
    ###
    --
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    --

    --
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

        self.size = size

    @property
    def size(self):
        """int: the lenth or width """
        return self.__size

    @size.setter
    def size(self, size):
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

    def my_print(self):
        """ prints in stdout the square with the character #
        Note:
            if size is equal to 0, print an empty line
        """

        if self.__size == 0:
            print()
        else:
            _pr = [
                ['#' for i in range(self.__size)]
                for j in range(self.__size)
            ]

            for array in _pr:
                for hash in array:
                    print(hash, end='')
                print()
