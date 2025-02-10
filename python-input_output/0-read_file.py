#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file and prrints it to stdout"""
    with open(filename, encoding='UTF-8') as a_file:
        print_content = a_file.read()
        print(print_content, end='')
