#!/usr/bin/python3
"""Defines a function that represents Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of integers that represent pascals triangle
      based on input of n (int)"""

    if n <= 0:
        return []

    else:
        triangle = [[1]]  # row 0

        # start at row 1 go until n-1
        for row in range(1, n):
            # start each row with 1
            row_start = [1]
            # get correct num of middle elements, go until row-1
            for column in range(1, row):
                # get the value of the nums based on the position in prev row
                row_start.append(triangle[row - 1][column - 1]
                                 + triangle[row - 1][column])
            # add 1 to the end
            row_start.append(1)
            # add to new row list to the triangle list
            triangle.append(row_start)
        return triangle
