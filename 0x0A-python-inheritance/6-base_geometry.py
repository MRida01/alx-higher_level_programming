#!/usr/bin/python3
"""Module that has an empty class."""

class BaseGeometry:
    """Empty class representing the base geometry."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
