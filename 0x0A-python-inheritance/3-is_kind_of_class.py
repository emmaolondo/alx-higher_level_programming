#!/usr/bin/python3
""" checks if object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is an instance of
    or if the object is an instance of a class that inherited from
    Attributes:
         param1: obj
         param2: a_class
    Return:
        True is instance of object or inherited from class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
