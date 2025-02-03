#!/usr/bin/python3
"""This module 1-my_list supplies a class `MyList`, with a method that
prints a sorted list in ascending order.
"""


class MyList(list):
    def print_sorted(self):
        """Prints a copy of a list in ascending order"""
        print(sorted(self))
