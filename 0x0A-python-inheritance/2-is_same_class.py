#!/usr/bin/python3
"""checks if an object is an instance of a specific class """


def is_same_class(obj, a_class):
    """ checks if an object is an instance of a class
    Args:
         obj: The object to be checked
         a_class: The class to confirm with

    Returns:
         True if the object(obj) is an instance of a class (a_class)
         otherwise False
    """
    if type(obj) is a_class:
        return True
    else:
        False
