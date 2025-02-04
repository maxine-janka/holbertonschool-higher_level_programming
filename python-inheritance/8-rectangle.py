#!/usr/bin/python3
"""This module ``8-rectangle`` supplies a class BaseGeometry and subclass Rectangle."""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """An area method that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value, width, height):
        """Validates whether value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format(width))
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format(height))
        if value <= 0 and width <= 0 and height <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Defines a Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    