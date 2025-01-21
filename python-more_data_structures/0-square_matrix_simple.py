#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda num: num * num, row)) for row in matrix]
    return (new_matrix)

# map(lamba num: num * num, row)
# map applies lamba function to every number in the row
