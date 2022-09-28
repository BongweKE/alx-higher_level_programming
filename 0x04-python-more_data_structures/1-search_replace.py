#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that replaces all occurrences of an element by another
    in a new list.

    Specifics:
        my_list is the initial list
        search is the element to replace in the list
        replace is the new element

    Requirements:
        You are not allowed to import any module
    """

    if my_list is None:
        return None
    else:
        return [replace  if x == search else x for x in my_list]
