#!/usr/bin/python3
"""This module creates a class Square that defines a square"""


class Square:
    """Square class with a private instance attribute.

    Attributes:
        __size (int): size of a square's side
    """
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of the square's side

        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
