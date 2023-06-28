#!/usr/bin/python3
""" Define class Square """


class Square:
    """ Define class square with private size attribute, area function
    """
    def __init__(self, size=0):
        """ Instatiation method with an optional size
        Handles and raises error messages in case an error occurs

        args:
            size (int): size attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Find the area of the current square """
        area = self.__size ** 2
        return area
