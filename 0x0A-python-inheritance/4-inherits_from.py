#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module for inherits_from() function"""


def inherits_from(obj, a_class):
    """A function tha check is a pnject is an instance of a class
    that inherited directly or indirectly from the specified class
    Attrs:
        obj (obj): the instance to check
        a_class (class): the super super class to check against

    Return:
        True or false
    """
    if not type(obj) is a_class:
        return issubclass(type(obj), a_class)
    return False
