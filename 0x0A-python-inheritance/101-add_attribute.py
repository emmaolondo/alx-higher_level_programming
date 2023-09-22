#!/usr/bin/python3
""" Defines a function that adds a new attribute to an object """


def add_attribute(obj, attr, val):
    """ Add a new attribute to an object if possible
    Args:
        obj (any): the object to be added
        attr (str): The name of the attribute
        val (any): The value of the attribute

    Raises:
        TypeError: If the object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
