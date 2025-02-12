#!/usr/bin/python3
"Defines a function that converts an instance of a class to a dictionary"


def class_to_json(obj):
    """Returns the dictionary representation of an object's attributes"""
    return obj.__dict__
