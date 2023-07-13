#!/usr/bin/python3
""" class that inherits from inbuilt class List """


class MyList(list):
    """ class that inherists from list """

    def __init__(self):
        """ initialises an object """
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
