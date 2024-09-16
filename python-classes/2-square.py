#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """Square class with a private instance attribute."""

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of the square's side

        Returns:
            None
        """
        self.__size = size
