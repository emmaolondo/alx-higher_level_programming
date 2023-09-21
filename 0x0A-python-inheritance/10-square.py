#!/usr/bin/python3
""" Defining a Square class that inherits from the Rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defining the Square class """
    def __init__(self, size):
        """" Instantiating the size of the square
        Args:
            size (int); private size of Square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self._size = size

    def area(self):
        """ Calculate the area of the Square"""
        return self._size ** 2
