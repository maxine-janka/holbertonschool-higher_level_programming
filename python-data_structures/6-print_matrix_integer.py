#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        length = len(i)
        counter = 1
        for j in i:
            if counter < length:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))
            counter += 1
