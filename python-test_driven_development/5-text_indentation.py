#!/usr/bin/python3
"""
This module supplies one function, `text_indentation(text)`,
that prints text with two new lines after each of the following
characters . ? and :
"""


def text_indentation(text):
    """
    Prints two new lines after a . ? or : in a
    given passage of text.

    Args:
        text(str): A string of text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""
    for char in text:
        new_text += char  # Acquire chars
        if char == '.' or char == ':' or char == '?':
            # If it finds .:?, print text and remove trailing space
            print(new_text.strip())
            print()
            new_text = ""  # Reset new line
    # handle left over text with no .:?
    if new_text:
        print(new_text.strip(), end="")
