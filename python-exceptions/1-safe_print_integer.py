#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError):
        return False

# :d to ensure value = int. Could use isinstance() in if statement as well.
