#!/usr/bin/python3
"""module that adds command-line arguments to a Python list and saves them to a JSON file."""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = 'add_item.json'

def main():

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
