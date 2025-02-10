#!/usr/bin/python3


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the
    number of characters added. Creates a new file if it doesn exist"""
    with open(filename, mode='a', encoding='UTF-8') as a_file:
        return a_file.write(text)
