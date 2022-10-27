#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """ a function that checks if the object is an instance of, or if an
    object is an instance of a class that inherited from, the specified class

    Attrs:
        obj (obj): The object
        a_class (class): A class to cross check

    Return:
        True if isinstance, otherwise False
    """
    return isinstance(obj, a_class)
