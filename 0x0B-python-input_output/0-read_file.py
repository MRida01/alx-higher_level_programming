#!/usr/bin/python3
"""Module to read a text file and print its contents to stdout."""

def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The path to the text file to be read. Defaults to "".

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
