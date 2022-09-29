#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary with all values multiplied by 2

    Requirements:
        1. You can assume that all values are only integers
        2. Returns a new dictionary
        3. You are not allowed to import any module
    """
    if a_dictionary is None:
        temp = None
    else:
        temp = {k: v*2 for k, v in a_dictionary.items()}

    return temp
