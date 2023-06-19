#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return (None)
    else:
        max_list = [my_list[0]]
        for i in my_list:
            if i > max_list[0]:
                max_list[0] = i
        return(max_list[0])
