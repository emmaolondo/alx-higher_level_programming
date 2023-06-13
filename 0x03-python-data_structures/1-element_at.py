#!/usr/bin/python3
"""
element_at - a function that retrieves an element from a list like in C
@my_list: The list to be printed
@idx: index
return: element at a specific index else None
"""
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
