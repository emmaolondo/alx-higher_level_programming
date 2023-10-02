#!/usr/bin/python3
"""Divide all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divide elements of matrix """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(error)
    if not isinstance(matrix, list):
        raise TypeError(error)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(error)
        for i in lists:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(error)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(error)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
