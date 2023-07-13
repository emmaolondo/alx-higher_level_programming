#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly
    an instance of the specified
    Attributes:
         param1: obj
         param2: a_class
    Return:
       True if the object is an instance
    """
    if type(obj) == a_class:
        return True
    else:
        return False
