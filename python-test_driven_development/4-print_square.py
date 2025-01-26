#!/usr/bin/python3
"""
This module supplies one function, `print_square(size)`,
that prints a square with the character '#' of a given size."
"""


def print_square(size):
    """
    Prints a square using the '#' character of a given size.

    Args:
        size(int): The length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
