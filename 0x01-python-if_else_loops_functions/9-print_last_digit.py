#!/usr/bin/python3
# function that prints the last digit of a number
def print_last_digit(number):
    number = abs(number)
    mod = number % 10
    print(f"{mod:d}", end="")
    return (mod)
