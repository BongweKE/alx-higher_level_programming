#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    return sum(set(my_list))
