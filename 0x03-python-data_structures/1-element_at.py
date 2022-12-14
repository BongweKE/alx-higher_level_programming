#!/usr/bin/python3
def element_at(my_list, idx):
    """function that retrieves an element from a list like in C.

    Requirements:
        If idx is negative, the function should return None
        If idx is out of range (> of number of element in my_list),
        the function should return None
        You are not allowed to import any module
        You are not allowed to use try/except

    Return:
        Value of element at the index or none
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
