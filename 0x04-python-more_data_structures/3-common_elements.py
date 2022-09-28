#!/usr/bin/python3
def common_elements(set_1, set_2):
    """A function that returns a set of common elements in two sets.

    You are not allowed to import any module
    """
    if set_1 is None or set_2 is None:
        pass
    else:
        return set_1.intersection(set_2)
