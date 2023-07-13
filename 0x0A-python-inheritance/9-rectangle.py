#!/usr/bin/python3
""" Inherists from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ instanstiation of the Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """find the area """
        return self.__width * self.__height

    def __str__(self):
        """ using __str__"""
        w = str(self.__width)
        h = str(self.__height)
        return ("[Rectangle] "+ w + "/" + h)
