#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""init file for models. When we call the models package,
this is the starting point
"""

class Base:
    """Base class for most of our classes"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
