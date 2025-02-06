#!/usr/bin/python3
"""This module demonstrates mixins to combine behaviours"""


class SwimMixin:
    """A class to show a creature that swims"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """A class to show a creature that flys"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars")
