#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """A function that deletes a key in a dictionary.

    Requirements:
    1. key argument will be always a string
    2. If a key doesn’t exist, the dictionary won’t change
    3. You are not allowed to import any module
    """
    if a_dictionary is None:
        return None

    if key in a_dictionary:
        del a_dictionary[key]
    else:
        pass
    return a_dictionary
