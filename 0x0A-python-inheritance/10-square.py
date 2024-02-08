#!/usr/bin/python3
"""Module that generates a square class."""

class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize the Square with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculate the area of the Square."""
        return self.__width * self.__height
