#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """A function that returns a list with all values multiplied by a
    number without using any loops.

    Returns:
        new list:

    Requirements:
        1. Same length as my_list
        2. Each value should be multiplied by number
        3. Initial list should not be modified
        4. You are not allowed to import any module
        5. You have to use map
        6. Your file should be max 3 lines
    """
    if my_list is None or number is None:
        pass
    else:
        r = list(map(
            (lambda x: x * number),
            my_list
        ))
        return r
