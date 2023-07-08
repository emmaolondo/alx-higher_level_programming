#!/usr/bin/python3
""" Defining rectangle class """


class Rectangle:
    """ Handling the Rectangle class eith getters and setters """
    def __init__(self, width=0, height=0):
        """ instatiation with an optional width and height """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """ retriving the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height  using setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ retriving the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ using setter method to set the height """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
