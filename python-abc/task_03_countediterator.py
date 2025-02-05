#!/usr/bin/python3
"""This module customizes the behaviour of the iterator object"""


class CountedIterator:
    """Extends the built-in iterator to keep track of iterations"""

    def __init__(self, some_iterable):
        """Initialise the CountIterator with an interable object"""
        self.iterator = iter(some_iterable)
        self.counter = 0

    def __next__(self):
        """Overrides the next method by returning the next item
        from the iterator and incrementing the counter"""

        try:
            item = next(self.iterator)
            self.counter += 1
            return item

        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Returns the current number of items iterated"""
        return self.counter
