#!/usr/bin/python3
""" A function that finds the peak of unsorted integers in a list """



def find_peak(list_of_integers):
    """ find the peak """
    if list_of_integers == []:
        return None

    for i in range(len(list_of_integers) - 1):
        if list_of_integers[i] >= list_of_integers[i + 1] and list_of_integers[i] >= list_of_integers[i - 1]:
            return list_of_integers[i]
