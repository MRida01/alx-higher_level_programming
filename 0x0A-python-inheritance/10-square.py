#!/usr/bin/python3
"""Module containing Square class inheriting from Rectangle."""

class Square(Rectangle):
    """Square class inheriting from Rectangle.

    Attributes:
        size (int): Size of the square.

    Methods:
        __init__(self, size): Initializes the Square with size.
        __str__(self): Returns a string representation of the Square.
        area(self): Calculates the area of the Square.
    """

    def __init__(self, size):
        """Initialize the Square with size.

        Args:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] {}/{}".format(self.width, self.height)

    def area(self):
        """Calculate the area of the Square."""
        return self.width * self.height
