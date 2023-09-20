#!/usr/bin/python3
""" Defining a BaseGeometry class """


class BaseGeometry:
    """Defining the BaseGeometry with properties """
    def area(self):
        """Raise an exceltion"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ fuction that validates a value the name is always a string
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
