#!/usr/bin/python3
"""This module ``2-is_same_class`` supplies a single method that
checks the class of an object
"""


def is_same_class(obj, a_class):
    """Check if an object is an exact instance of a given class"""
    if type(obj) is a_class:
        return True
    else:
        return False
