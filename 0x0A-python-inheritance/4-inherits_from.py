#!/usr/bin/python3
"""Only sub class of """


def inherits_from(obj, a_class):
    """ vheck if an object is inherited direcl
    or indirectly from a specifi class
    Return:
        True otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
