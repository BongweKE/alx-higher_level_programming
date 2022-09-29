#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """A function that prints a dictionary by ordered keys.

    You can assume that all keys are strings

    Requirements:
        1. Keys should be sorted by alphabetic order
        2. Only sort keys of the first level
        (don’t sort keys of a dictionary inside the main dictionary)
        3. Dictionary values can have any type
        4. You are not allowed to import any module
    """
    if a_dictionary is not None:
        for key in sorted(a_dictionary):
            print(f"{key}: {a_dictionary[key]}")
