#!/usr/bin/python3
""" a class Square that inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defining the class square """

    def __init__(self, size):
        """instatiation of size """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
