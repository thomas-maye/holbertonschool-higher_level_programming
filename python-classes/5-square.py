#!/usr/bin/python3
"""This module defines a class Square."""


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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """int: size of a square's side"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
