#!/usr/bin/python3
def uppercase(s):
    """prints a string in uppercase, followed by a new line."""
    for c in s:
        if (ord(c) >= 97 and ord(c) <= 122):
            c = chr(ord(c) - 32)
        print('{0}'.format(c), end="")
    print("")