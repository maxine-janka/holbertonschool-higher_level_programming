#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Defines a Student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiate Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            #  To store filtered attrs
            new_dict = {}
            # Iterate each attr in list
            for att in attrs:
                #  Check if attr exists
                if hasattr(self, att):
                    # Store its value in the new dict
                    new_dict[att] = getattr(self, att)
            return new_dict

    def reload_from_json(self, json):
        """Replaces attributes of a Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
