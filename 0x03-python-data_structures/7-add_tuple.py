#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds 2 tuples.

    Returns:
        a tuple with 2 integers
    Requirements:
        1. The first element should be the addition of the first
        element of each argument
        2. The second element should be the addition of the second
        element of each argument
        3. You are not allowed to import any module
        4. You can assume that the two tuples will only contain integers
        5. If a tuple is smaller than 2, use the value 0 for each
        missing integer
        6. If a tuple is bigger than 2, use only the first 2 integers
    """

    len_a, len_b = len(tuple_a), len(tuple_b)
    if len_a > 1:
        a_0, a_1 = tuple_a[0], tuple_a[1]
    elif len_a == 1:
        a_0 = tuple_a[0]
        a_1 = 0
    elif len_a == 0:
        a_0, a_1 = 0, 0

    if len_b > 1:
        b_0, b_1 = tuple_b[0], tuple_b[1]
    elif len_b == 1:
        b_0 = tuple_b[0]
        b_1 = 0
    elif len_b == 0:
        b_0, b_1 = 0, 0

    return (a_0 + b_0, a_1 + b_1)
