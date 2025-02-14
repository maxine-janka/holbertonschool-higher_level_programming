#!/usr/bin/python3
"""A basic serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """Serilizes the given data and saves to a file"""
    with open(filename, mode="w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Deserialise and load data from a given file"""
    with open(filename, mode="r") as file:
        return json.load(file)
