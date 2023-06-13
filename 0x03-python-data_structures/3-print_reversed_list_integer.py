#!/usr/bin/bash
# function that prints all integers in a list in a reversed order

def print_reversed_list_integer(my_list=[]):
    plen = len(my_list)
    for i in range(plen - 1, -1, -1):
        print("{}".format(my_list[i]), end="\n")
