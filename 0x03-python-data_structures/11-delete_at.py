#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """A function that deletes the item at a specific position in a list.

    Requirements:
        1. If idx is negative or out of range,
        nothing changes (returns the same list)
        2. You are not allowed to use pop()
        3. You are not allowed to import any module

    Return:
        same or modified list
    """
    if idx >= len(my_list):
        pass
    else:
        del my_list[idx]
    return my_list
