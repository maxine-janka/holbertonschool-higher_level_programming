#!/usr/bin/python3
import sys
if __name__ == "__main__":

    length = len(sys.argv)
    sum = 0

    if length == 0:
        print("0")

    else:
        for i in range(1, length):
            sum += int(sys.argv[i])
        print("{}".format(sum))
