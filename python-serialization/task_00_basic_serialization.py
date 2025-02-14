#!/usr/bin/python3
"""A basic serialization module"""

import pickle


def serialize_and_save_to_file(data, filename):
    """Serilizes the given data and saves to a file"""
    with open(filename, mode="wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """Deserialise and load data from a given file"""
    with open(filename, mode="rb") as file:
        return pickle.load(file)
