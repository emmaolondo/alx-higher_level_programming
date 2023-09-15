#!/usr/bin/python3
""" a class MyList that inherits from list """


class MyList(list):
    """ The inherited class """
    def print_sorted(self):
        """ public method tat prints the list but in ascending order """
        print(sorted(self))
