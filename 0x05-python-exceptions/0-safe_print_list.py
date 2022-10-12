#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            if j < x and x > 0:
                print(f"{i}", end='')
                j += 1
            else:
                print()
                return j
        print()
    except BaseException as err:
        raise
    return j
