#!/usr/bin/python3
# print the hexadecimal equivalent of a number
for h in range(0, 99):
    hexa = f"{h:x}"
    print("{} = 0x{}".format(h, hexa))
