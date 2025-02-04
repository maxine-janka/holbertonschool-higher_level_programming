#!/usr/bin/python3
"""This module ``8-rectangle`` supplies a class BaseGeometry and subclass Rectangle."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a Rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
