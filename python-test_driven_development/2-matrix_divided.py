#!/usr/bin/python3
"""
This module supplies one function, `matrix_divided(matrix, div)`,
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix: (list). A list of lists of integers or floats to dicvide.
        b: (int or float) The divisor.

    Returns:
        The resulting new list.
    """
    new_list = []
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Matrix must be a 2D list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    # Rows in the list must be a list
    for row in matrix:
        # Rows must be same size
        if len(row) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size")
        # Rows must me a list
        if not isinstance(row, list):
            raise TypeError(error_msg)

        # Elements in the row must be an in or float
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

        # div must be an int or float
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

    # element = i, otherwise line space too long
    new_list = [[round(i / div, 2) for i in row] for row in matrix]
    return new_list
