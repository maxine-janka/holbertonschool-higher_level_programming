#!/usr/bin/python3
def uppercase(str):
    """"
    Prints a string in uppercase, followed by a new line.

    Parameters:
        str: The string to print in uppercase.
    """
    for char in str:  # Iterate through str by chars
        letter = ord(char)  # Return int for unicode char
        if letter >= 97 and letter <= 122:
            char = chr(letter - 32)  # Convert back to uppercase char
        print(char, end="")
    print()
