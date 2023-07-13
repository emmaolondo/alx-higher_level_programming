#!/usr/bin/python3
""" checks if an object is an instance of a class """


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    Attribute:
        param1: obj
        param2: a_class

    Return:
        True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
