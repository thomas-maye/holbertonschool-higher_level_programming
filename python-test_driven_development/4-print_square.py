#!/usr/bin/python3
""" Module for print_square method """


def print_square(size):
    """ Method to print a square with the character #
    Args:
        size: size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
    return
