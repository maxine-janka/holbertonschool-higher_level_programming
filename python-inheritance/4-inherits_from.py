#!/usr/bin/python3
"""This module ``4-inherits_from`` supplies a single method that
checks if the object is an instance of a class that inherited
(directly or indirectly) from a given class.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class (direct or indirect)"""
    if issubclass(type(obj), a_class) and not (type(obj) is a_class):
        return True
    else:
        return False
