#!/usr/bin/python3
# function that prints all integers in a list in a reversed order

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        plen = len(my_list)
        for i in range(plen - 1, -1, -1):
            print("{:d}".format(my_list[i]), end="\n")
