#!/usr/bin/python3
""" function that returns the lidt of available attributes """


def lookup(obj):
    """
    function that returns the list of available
    attributes and methods of an object
    """
    return (dir(obj))