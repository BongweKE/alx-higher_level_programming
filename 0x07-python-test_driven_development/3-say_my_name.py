#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A module to print out names"""


def say_my_name(first_name, last_name=""):
    """A function to print the name of given being"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
