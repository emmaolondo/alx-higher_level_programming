#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    else:
        c = sys.argv[2]
        if c != '+' and c != '-' and c != '*' and c != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            if sys.argv[2] == '+':
                print("{} {} {} = {}".format(a, b, sys.argv[2], add(a, b)))
            elif sys.argv[2] == '-':
                print("{} {} {} = {}".format(a, b, sys.argv[2], sub(a, b)))
            elif sys.argv[2] == '*':
                print("{} {} {} = {}".format(a, b, sys.argv[2], mul(a, b)))
            elif sys.argv[2] == '/':
                print("{} {} {} = {}".format(a, b, sys.argv[2], div(a, b)))


