#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order.

    Requirements:
        Format: one integer per line.
        1. You are not allowed to import any module
        2. You can assume that the list only contains integers
        3. You are not allowed to cast integers into strings
        4. You have to use str.format() to print integers

    """
    for i in reversed(my_list):
        print("{:d}".format(int(i)))
