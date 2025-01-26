#!/usr/bin/python3
"""
This module supplies one function, `add_integer(a, b=98)` that adds two integers.
"""
def add_integer(a, b=98):
    """
    Adds two integers and returns the sum.

    Args:
        a: (int) The first integer.
        b: (int) The second integer.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
