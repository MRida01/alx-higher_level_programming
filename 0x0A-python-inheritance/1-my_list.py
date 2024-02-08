#!/usr/bin/python3
"""Module that wrints a list sorted in ascending order."""

class MyList(list):
    """A subclass of list with additional method print_sorted."""
    
    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
