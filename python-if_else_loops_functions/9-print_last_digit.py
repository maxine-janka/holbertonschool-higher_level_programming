#!/usr/bin/python3
def print_last_digit(number):
    """"
    Prints the last digit of a number and returns the value.
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
