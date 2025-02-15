#!/usr/bin/python3
"""Serializing and Deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a dictionary to XML and saves to a file"""
    # Create root element
    root = ET.Element('data')

    for key, value in dictionary.items():
        element = ET.Element(key)  # Create element from key
        element.text = str(value)  # Set innertext to value
        root.append(element)

    # Create element tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Reconstructs a dictionary from an XML file"""
    # create tree object from XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for element in root:
        key = element.tag
        value = element.text
        dictionary[key] = value
    return dictionary
