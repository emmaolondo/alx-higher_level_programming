#!/usr/bin/pyrhon3
""" Write an object to a text file using a JON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
    using a JSON representation

    Args:
         my_obj - object to be written
         filename - file to be written into
    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
