#!/usr/bin/python3
"""This module 0-lookup supplies one function, `lookup(obj)`,
that returns a list of available attributes and methods of an object.
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return list(dir(obj))
