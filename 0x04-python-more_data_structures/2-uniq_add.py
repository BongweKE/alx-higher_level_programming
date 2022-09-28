#!/usr/bin/python3
def uniq_add(my_list=[]):
    """A function that adds all unique integers in a list
    (only once for each integer).

    Requirements:
        You are not allowed to import any module

    Return:
        Sum
    """
    if my_list is None:
        return 0
    return sum(set(my_list))
