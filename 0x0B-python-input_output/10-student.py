#!/usr/bin/python3
""" Define a class Student """


class Student:
    """ Describe the class student"""
    def __init__(self, first_name, last_name, age):
        """ Class initialiasation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves the dictionary representation of a Student
        Args:
           attrs : attributes

        if attrs is a list of strings retrieve only attribute names contained
        in the list
        else all attributes must be retrived
        """
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
