#!/usr/bin/python3
""" Define a class Student """


class Student:
    """ Describe the class student"""
    def __init__(self, first_name, last_name, age):
        """ Class initialiasation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Function that retrieves the dictionary representation of
        a Student"""
        return self.__dict__
