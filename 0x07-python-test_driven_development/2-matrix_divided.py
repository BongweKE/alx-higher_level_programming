#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module with function to divide a matrix"""


def matrix_divided(matrix, div):
    """A function to divide all values of a matrix by a given value"""

    if (len(matrix) < 1):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    else:
        matrix_size = len(matrix[0])
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for val in row:
            if type(val) != int and type(val) != float:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        if len(row) != matrix_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round((val / div), 2) for val in row] for row in matrix]
