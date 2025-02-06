#!/usr/bin/python3
"""This module ``8-rectangle`` supplies a class Rectangle,
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
        #  Can also use self. instead of super()
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
