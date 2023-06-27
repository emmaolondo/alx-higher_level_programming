#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    l_len = 0
    for val in range(x):
        try:
            print("{:d}".format(my_list[val]), end="")
            l_len += 1
        except (TypeError, ValueError):
            val += 1
            continue
    print("")
    return l_len
