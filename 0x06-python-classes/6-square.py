#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Handling the class square with getters and setters """
    def __init__(self, size=0, position=(0, 0)):
        """ Instatiation of the square class while handling errors

        args:
          size(int): attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

        @property
        def position(self):
            """using getter to retrieve the position"""
            return self.__position

        @position.setter
        def position(self, value):
            """ sets the position of the square using a tuple """
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 posit\
                        ive integers")
            elif not isinstance(value[0], int) or not isinstance(value[1], int):
                raise TypeError("position must be a tuple of 2 positive integers")
            elif value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value

    def my_print(self):
        """ Prints the stdout of a square with # character """
        val = self.__size
        c = '#'
        if val != 0:
            for i in range(0, self.__position[1]):
                print("")
            for j in range(0, val):
                print("{}{}".format(' ' * self.__position[0], c * val))
        else:
            print("")
