#!/usr/bin/python3

if __name__ == "__main__":  # the code is not executed when imported
    import hidden_4
    names = dir(hidden_4)
    sort_name = sorted(n for n in name if not n.startswith("__"))
    for n in sort_name:
        print(n)
