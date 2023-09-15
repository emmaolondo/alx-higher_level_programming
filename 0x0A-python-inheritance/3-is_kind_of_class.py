#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """ check if the object is an instance of or
    if the object is an instance of a class that inherited from
    the specified class
    Args:
       obj: the object
       a_class: class

    Return:
         True if object is of the same class or inherited
         False: if otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
