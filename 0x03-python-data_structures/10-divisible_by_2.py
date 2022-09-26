#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list.

    Return:
        a new list with True or False
        depending on whether the integer at the same position in
        the original list is a multiple of 2

    Requirements:
        1. The new list should have the same size as the original list
        2. You are not allowed to import any module

    oneliner answer:
    return [x%2 == 0 for x in my_list]

    practise with lambda
    """
    val = list(map(
        lambda x: x % 2 == 0,
        my_list
    ))
    return val
