#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i_len = 0
    try:
        while i_len < x:
            print("{:d}".format(my_list[i_len]), end="")
            i_len += 1
    except IndexError:
        pass
    print("")
    return i_len
