#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        # format spec :, pad with 0, width of 2, dec int
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
