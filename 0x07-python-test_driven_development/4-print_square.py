#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A function to print a square out"""


def print_square(size):
    """Print a square out given it's length"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
