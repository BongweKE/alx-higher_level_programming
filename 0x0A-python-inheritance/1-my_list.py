#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module for MyList Class"""


class MyList(list):
    """A class that inherits from list"""
    def __init__(self):
        """Initialize the Mylist instances"""
        super().__init__()

    def print_sorted(self):
        """A function to print the list in a sorted manner"""
        print(sorted(self))
