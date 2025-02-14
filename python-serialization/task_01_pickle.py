#!/usr/bin/python3
"""Serialize and Deserialize a custom python object using pickle"""
import pickle


class CustomObject:
    """Defines a custom object"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints attributes in the given format"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serializes the current instance of an object"""
        try:
            with open(filename, mode='wb') as file:
                return pickle.dump(self, file) #  pass in file and object
        except pickle.PickleError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes and returns the object"""
        try:
            with open(filename, mode='rb') as file:
                return pickle.load(file)
        except pickle.UnpicklingError:
            return None
        except FileExistsError:
            return None
