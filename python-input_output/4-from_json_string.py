#!/usr/bin/python3
"""Defines a function that returns an object from a JSON string"""
import json


def from_json_string(my_str):
    """Returns an object from a JSON string (deserialization)"""
    return json.loads(my_str)
