#!/usr/bin/python3
def no_c(my_string):
    """function that removes all characters c and C from a string.

    Requirements:
        1. The function should return the new string
        2. You are not allowed to import any module
        3. You are not allowed to use str.replace()
    Return:
        string without letter c
    """
    return ''.join([letter for letter in my_string
                    if letter not in ('c', 'C')])
