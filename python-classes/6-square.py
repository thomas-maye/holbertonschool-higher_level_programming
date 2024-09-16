#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """Square class with a private instance attribute.

    Attributes:
        __size (int): size of a square's side
    """
    def __init__(self, size=0 , position=(0, 0)):
        """Initializes a square

        Args:
            size (int): size of the square's side

        Returns:
            None
        """
        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """int: size of a square's side"""
        return self.__size
    
    @property
    def position(self):
        """tuple: position of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print("_" * self.__position[0] + "#" * self.__size)
