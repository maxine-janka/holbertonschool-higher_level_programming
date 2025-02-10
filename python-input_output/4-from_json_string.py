#!/usr/bin/python3
import json


def from_json_string(my_str):
    """Returns an object from a JSON string (deserialization)"""
    return json.loads(my_str)
