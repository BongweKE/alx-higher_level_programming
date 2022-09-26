#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list at a specific position
    Requirements:
        a) If idx is negative, the function should not modify anything,
        and returns the original list
        b) If idx is out of range (> of number of element in my_list),
        the function should not modify anything, and returns the original list
        c) You are not allowed to import any module
        d) You are not allowed to use try/except

    Return val:
        Modified or original list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
