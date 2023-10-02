#!/usr/bin/python3
""" Return the JSON representation of an object """
import json


def to_json_string(my_obj):
    """ a function that returns the JSON representation of an object (string

    Arg:
       my_obj - the object to be converted

    Return:
        The JSON representation
    """
    return json.dumps(my_obj)
