#!/usr/bin/python3
""" A function that finds the peak of unsorted integers in a list """


def find_peak(list_of_integers):
    """ find the peak """
    a = list_of_integers[:]
    if a == []:
        return None

    for i in range(len(a) - 1):
        if a[i] >= a[i + 1] and a[i] >= a[i - 1]:
            return a[i]

    if a[-1] >= a[-2]:
        return a[-1]
