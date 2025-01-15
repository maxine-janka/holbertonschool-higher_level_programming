#!/usr/bin/python3
def islower(c):
    """"
    Checks for lowercase character.

    Parameters:
        c: The character the check.

    Returns:
        True: If lowercase
        False: Otherwise
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
