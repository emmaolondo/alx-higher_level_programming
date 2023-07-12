#!/usr/bin/python3
""" Defining rectangle class """


class Rectangle:
    """ Handling the Rectangle class eith getters and setters """
    def __init__(self, width=0, height=0):
        """ instatiation with an optional width and height """
        self.__height = height
        self.__width = width

    def area(self):
        """ Return the area """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        per = (2 * self.__width) + (2 * self.__height)
        return per

    @property
    def width(self):
        """ retriving the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setting the width using seter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retriving the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ using setter method to set the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def r_print(self):
        """print rectangle using the # character"""
        h = self.__height
        w = self.__width
        if h == 0 or w == 0:
            print('')
        return '\n'.join('#' * w for _ in range(h))

    def __str__(self):
        """using str to print rectangle """
        return f"{self.r_print()}"

    def __repr__(self):
        """ using the inbuilt __rep__ """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
