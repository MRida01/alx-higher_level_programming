#!/usr/bin/python3
"""Module that writes an object to a text file using a JSON representation."""

import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write the JSON representation to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
