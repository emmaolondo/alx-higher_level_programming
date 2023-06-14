#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length == 1:
        print(0)
    elif length == 2:
        print(sys.argv[1])
    else:
        total = 0
        for i in range(1, length):
            val = int(sys.argv[i])
            total = total + val
        print(total)
