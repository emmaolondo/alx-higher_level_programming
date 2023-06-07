#!/usr/bin/python3
# print all ASCII alphabet in lowercase except qe
for letter in range(97, 123):
    lower = "{}".format(chr(letter))
    if lower not in "qe":
        print(lower, end="")
