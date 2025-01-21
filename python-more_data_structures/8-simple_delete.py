#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    return a_dictionary

# None - nothing is deleted if a key isnt provided, no error occurs
