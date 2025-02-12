#!/usr/bin/python3
"""Defines a script to load, add and save arguments to a file"""

import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

myfile = "add_item.json"

#  If file exists then load data
if os.path.exists(myfile):
    mylist = load_from_json_file(myfile)

#  Otherwise create an empty list
else:
    mylist = []

#  Capture CL args and add the list
mylist.extend(sys.argv[1:])

#  Create and save back to a file
save_to_json_file(mylist, myfile)
