#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module to implement a function to add integers"""


def add_integer(a, b=98):
    """A function to add two integers

    Checks:
    1. raises TypeError if a, b are not ints or floats
    2. Type casts floats to ints before addition

    Returns: The sum of the two integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a, b = int(a), int(b)
    return a + b
