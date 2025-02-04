#!/usr/bin/python3
"""This module ``3-is_kind_of_class`` supplies a single method that
checks the class and subclass of an object
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or a subclass"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
