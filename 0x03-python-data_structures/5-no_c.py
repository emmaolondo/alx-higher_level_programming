#!/usr/bin/python
def no_c(my_string):
    string = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(string))