#!/usr/bin/python3
""" 0-square
    This module contains the class Square
"""


class Square:
    """This is the definition of Square
        Attributes:
            size (int): The size of the square, default is 0.
            position (int): The position of the square, default is (0,0)
            position[0] is the printed new lines before the square.
            position[1] is the printed spaces to the left of the square.
    """

    def __init__(self, size=0, position=(0,0)):
        """Initialises an instance of Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Caluclates and returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter method for size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square for a given size and position"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for space in range(self.size):
                print("a" * self.position[0], end="")
                for hash in range(self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        """Getter method for the position of the square"""
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
