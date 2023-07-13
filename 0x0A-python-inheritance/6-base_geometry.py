#!/usr/bin/python3
""" defining the BaseGeomety class """


class BaseGeometry:
    """ a class with a public instance method """
    def area(self):
        """ public instance method """
        raise Exception("area() is not implemented")
