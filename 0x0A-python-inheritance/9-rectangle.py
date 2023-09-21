#!/usr/bin/python3
""" Defining a class rectangle that inherits from the BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """" Decribing the child class i.e Rectangle using its properties """

    def __init__(self, width, height):
        """ Instatiating the width and height of a rectangle
        Args:
             width: private the width of rectangle
             height: private height of rectangle
             Both must be positive integers validated by integer_validator

        Return:
             The child class
        """
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height

    def area(self):
        """Return the area of the rectangle"""
        return self._width * self._height

    def __str__(self):
        """Print the properties of the rectangle """
        return f"[{str(self.__class__.__name__)}] {self._width}/{self._height}"
