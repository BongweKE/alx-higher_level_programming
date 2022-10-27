#!/usr/bin/python3
"""Module for lookup function """


def lookup(obj):
    """a function that returns the list of available attributes
    and methods of an object
    Attrs:
        obj(obj): An object
    """
    return(dir(obj))
