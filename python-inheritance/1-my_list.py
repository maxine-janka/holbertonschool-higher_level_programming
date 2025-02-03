#!/usr/bin/python3
"""This module 1-my_list supplies a class `MyList`, with a single method that
prints a sorted list in ascending order.
"""


class MyList(list):
    """A class MyList that inherits from list"""
    def print_sorted(self):
        """Prints a copy of a list in ascending order"""
        print(sorted(self))
