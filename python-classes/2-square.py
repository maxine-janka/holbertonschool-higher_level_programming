#!/usr/bin/python3
"""0-square
    This module contains the class square"""


class Square:
    """This is a definition of a square
        Attributes:
            size (int): Contains the length of a side of a square
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
