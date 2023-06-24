#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[num ** 2 for num in x]for x in matrix]
    return new_matrix
