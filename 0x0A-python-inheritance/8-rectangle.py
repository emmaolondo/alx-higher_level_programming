#!/usr/bin/python3
""" Inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Defining Rectangle class"""


class Rectangle(BaseGeometry):
    """Defining Rectangle """

    def __init__(self, width, height):
        """ instanstiation of the Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
