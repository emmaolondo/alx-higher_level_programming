#!/usr/bin/python3
""" Defining a class Square """


class Square:
    """ class Square that defines a square with private attribute size """
    def __init__(self, size=0):
        """ Function that initializes the class with an optional size attribute

        args:
           size (int): size attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
