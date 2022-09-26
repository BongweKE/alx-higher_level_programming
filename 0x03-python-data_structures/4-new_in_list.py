#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a specific position
    without modifying the original list (like in C).

    Requirements:
        1. If idx is negative, the function should return a copy of
        the original list
        2. If idx is out of range (> of number of element in my_list),
        the function should return a copy of the original list
        3. You are not allowed to import any module
        4. You are not allowed to use try/except

    Return:
        Original or Modified copy of the original list
    """

    temp = my_list[:]
    if idx < 0 or idx >= len(temp):
        return temp
    temp[idx] = element
    return temp
