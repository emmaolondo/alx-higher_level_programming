#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(0)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
    else:
        total = 0
        for i in range(1, len(sys.argv)):
            val = int(sys.argv[i])
            total = total + val
        print(total)
