#!/usr/bin/python3
"""This module demontrates multiple inheritance and method resolution order"""


class Fish:
    "A parent class Fish"

    def swim(self):
        print("The fish in swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    "A parent class Bird"

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    "A child class inheriting from Fish and Bird"

    def fly(self):
        print("The flying fish is soaring")

    def swim(self):
        print("The flying fish is swimming")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
