#!/usr/bin/python3

# Defining the Rectangle class using getters and setters
class Rectangle:
    """ Initializing the instance attributes width and height """
    def __init__(self, width=0, height=0):
        """ Initialize private attributes """
        self.width = width
        self.height = height

    """Private attribute : height"""
    @property
    def height(self):
        """Getting the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height""
        value = self.__height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Private instance attribute : width"""
    @property
    def width(self):
        """Getting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width
        value = self.__width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        per = 2 * (self.__height + self.__width)
        if self.height == 0 or self.__width == 0:
            per = 0
        return per
