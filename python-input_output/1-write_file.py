#!/usr/bin/python3
"""A function that overwrites a files contents"""


def write_file(filename="", text=""):
    """Overwrites the content of a file and returns
    the number of characters written. Creates a new file if it doesnt exit"""
    with open(filename, mode='w', encoding='UTF-8') as a_file:
        return a_file.write(text)

#  write returns number of chars not bytes in text mode
