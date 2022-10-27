#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module for is_same_class() function"""


def is_same_class(obj, a_class):
    """a funtion to test whether an object is an instance of a
    given class
    Attrs:
        obj (obj): The object to test
        a_class (class): A class to test against

    Returns:
        True if it's an instance, False if not
    """
    if isinstance(obj, a_class):
        return type(obj) is a_class
    return False
