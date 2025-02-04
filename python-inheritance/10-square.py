#!/usr/bin/python3
"""This module ``10-square`` supplies a class Square,
 that inherits from Rectangle."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a Square from Rectangle."""
    def __init__(self, size):
        """Initialises a Square
        Args:
        size (int): The size of a square.
        """
        super().integer_validator("size", size)
        #  Call Rectangles constructor to access private height and width
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
