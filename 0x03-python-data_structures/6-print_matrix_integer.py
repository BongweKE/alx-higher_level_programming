#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """A function that prints a matrix of integers.

    Requirements:
    1. You are not allowed to import any module
    2. You can assume that the list only contains integers
    3. You are not allowed to cast integers into strings
    4. You have to use str.format() to print integers
    """

    for row in matrix:
        for item in row:
            print("{:s}{:d}".format('' if row.index(item) == 0
                                    else ', ',
                                    int(item)),
                  end='')
        print()
