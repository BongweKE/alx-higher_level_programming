#!/usr/bin/python3
def max_integer(my_list=[]):
    """A function that finds the biggest integer of a list.

    Requirements:
        1. If the list is empty, return None
        2. You can aassume that the list only contains integers
        3. You are not allowed to import any module
        4. You are not allowed to use the builtin max()

    Return:
        Biggest integer or None
    """
    if len(my_list) == 0:
        return None
    else:
        return sorted(my_list)[-1]
