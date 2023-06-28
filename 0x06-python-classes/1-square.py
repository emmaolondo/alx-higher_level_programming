#!/usr/bin/python3
""" Write a class Square that defines a square """


class Square:
    """ Class based on:
    Attributes:
          size a private attribute.
    """
    def __init__(self, size):
        """ Initializes the square.

        Args:
          size(int): The private size of the square
        """
        self.__size = size
