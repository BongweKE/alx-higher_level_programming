#!/usr/bin/python3
def is_none(a_dictionary):
    """Check if our dictionary has all vals as None
    Return:
        True or False
    """
    if a_dictionary is None:
        return True

    s = sum(
        [1 if x is not None else 0 for x in list(a_dictionary.values())])

    if s == 0:
        return True
    else:
        return False


def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value.

    Requirements:
        1. You can assume that all values are only integers
        2. If no score found, return None
        3. You can assume all students have a different score
        4. You are not allowed to import any module
    """

    if is_none(a_dictionary):
        return None
    val = max(a_dictionary.values())
    for key in a_dictionary.keys():
        if a_dictionary[key] == val:
            return key

    return None
