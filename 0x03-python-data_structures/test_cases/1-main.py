#!/usr/bin/python3
element_at = __import__('0x03-python-data_structures/-element_at').element_at

my_list = [1, 2, 3]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
