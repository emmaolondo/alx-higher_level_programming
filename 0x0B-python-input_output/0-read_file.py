#!/usr/bin/python3
""" A function that reads a text file(UTF8) and prints its stdout """


def read_file(filename=""):
    """ Reads a text file and prints ints stdout
    Args:
       filename: name of the textfile to be accessed
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
