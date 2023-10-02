#!/usr/bin/python3
""" The pascal triangle implementation """


def pascal_triangle(n):
    """function that returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []
    res = [[1]]

    while len(res) != n:
        row = [1]
        temp = res[-1]
        for i in range(len(temp) - 1):
            row.append(temp[i] + temp[i + 1])
        row.append(1)
        res.append(row)
    return res
