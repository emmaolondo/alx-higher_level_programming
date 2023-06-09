#!/usr/bin/python3
if __name__ == "__main__":
    """ Read and print number of arguments. """
    import sys
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
