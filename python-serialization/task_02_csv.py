#!/usr/bin/python3
"""A function convertinf CVS data to JSON"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts CVS data to JSON format"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            dict_list = list(csv.DictReader(csv_file))
        with open("data.json", mode='w', encoding='utf-8') as data_file:
            json.dump(dict_list, data_file)
            return True
    except FileNotFoundError:
        return False
