#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """a function that prints the first x elements of a list and only integers.

    Requirements:
    - my_list can contain any type (integer, string, etc.)
    - All integers have to be printed on the same line followed by a new line
        - other type of value in the list must be skipped (in silence).
    - x represents the number of elements to access in my_list
    - x can be bigger than the length of my_list
        - if it’s the case, an exception is expected to occur
    - You have to use try: / except:
    - You have to use "{:d}".format() to print an integer
    - You are not allowed to import any module
    - You are not allowed to use len()

    Returns
    - the real number of integers printed
    """

    size_c, print_c = 0, 0
    try:
        while size_c < x:
            if x > 0 and type(my_list[size_c]) is int:
                try:
                    print("{:d}".format(my_list[size_c]), end='')
                except IndexError:
                    raise
                size_c += 1
                print_c += 1
            else:
                size_c += 1
                continue
        print()
        return print_c
    except BaseException:
        raise
