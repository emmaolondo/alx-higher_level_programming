#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Handling the class square with getters and setters """
    def __init__(self, size=0):
        """ Instatiation of the square class while handling errors

        args:
          size(int): attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Finds the area of a square """
        area = self.__size ** 2

    @property
    def size(self):
        """ Function that gets/ retrieves the size of a square """
        return self.__size

    @size.setter
    def size(self, value):
        """ function tha sets the value of the size of a square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Prints the stdout of a square with # character """
        val = self.__size
        c = '#'
        for i in range(val):
            print(c * val, end='')
            print('')
        if val == 0:
            print('')
