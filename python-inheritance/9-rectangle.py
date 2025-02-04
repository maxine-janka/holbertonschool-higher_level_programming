#!/usr/bin/python3
"""This module ``9-rectangle`` supplies a class Rectangle,
 a subclass of BaseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """Initialises a Rectangle.

        Args:
        width (int): The width of a new Rectangle.
        height (int): The height of a new Rectangle.

        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of a Rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Returns a string representation of width / height of a Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
