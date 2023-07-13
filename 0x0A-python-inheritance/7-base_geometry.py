#!/usr/bin/python3
class BaseGeometry:
    """ a class with a public instance method """
    def area(self):
        """ public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validates a value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
