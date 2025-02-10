#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, encoding='UTF-8') as a_file:
        print_content = a_file.read()
        print(print_content, end='')
