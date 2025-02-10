#!/usr/bin/python3
"""Defines a function that returns a JSON representation of an object"""
import json


def to_json_string(my_obj):
    """Returns a JSON string (Serialization)"""
    return json.dumps(my_obj)
