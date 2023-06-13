#!/usr/bin/python3
# A fuction that prints all integers of a list
# @my_list: list to be printed
# Return: one integer per line

def print_list_integer(my_list=[]):
    plen = len(my_list)  # get the lenght of the list
    for i in range(0, plen):
        print("{}".format(my_list[i]), end="\n")
