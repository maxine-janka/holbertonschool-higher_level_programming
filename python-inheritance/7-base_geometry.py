#!/usr/bin/python3
"""This module ``7-base_geometry`` supplies an empty class BaseGeometry,
an area method area that is not implemented and an integer validator."""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """An area method that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates whether value is an integer"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
