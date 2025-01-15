#!/usr/bin/python3
for i in range(0, 10):  # first number
    for j in range(0, 10):  # second number
        if i < j and i != j:  # condition for unique number
            # last pair
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
            else:
                print("{}{}".format(i, j), end=", ")
