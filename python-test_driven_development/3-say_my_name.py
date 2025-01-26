#!/usr/bin/python3
"""
This module supplies one function, `say_my_name(first_name, last_name="")`,
that prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Args:
        first_name (str):. Given string for first name.
        last_name (str): Given string for last name, default as empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
