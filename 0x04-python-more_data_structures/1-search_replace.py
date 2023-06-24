#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced_val = [replace if val == search else val for val in my_list]
    return replaced_val
