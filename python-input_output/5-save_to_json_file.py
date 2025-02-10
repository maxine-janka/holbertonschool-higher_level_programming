#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation"""
    with open(filename, mode='w', encoding='UTF-8') as a_file:
        json_str = json.dumps(my_obj)
        return a_file.write(json_str)
