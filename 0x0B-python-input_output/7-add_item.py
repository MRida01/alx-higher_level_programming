#!/usr/bin/python3
"""
Module: 7-add_item

This module provides a script to add all command-line arguments to a Python list
and save them to a file in JSON format.

Usage:
    ./7-add_item.py [argument1] [argument2] ...

Arguments:
    - [argument1], [argument2], ... : Any number of arguments to be added to the list.

The list is saved as a JSON representation in a file named add_item.json. If the file
does not exist, it will be created.

Functions:
    No functions are directly exposed by this module.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = 'add_item.json'

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
