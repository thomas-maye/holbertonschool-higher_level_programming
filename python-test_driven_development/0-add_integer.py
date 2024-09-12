#!/usr/bin/python3
def add_integer(a, b=98):

    """
    Function that adds 2 integers.
    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The sum of the 2 integers.

    Raises:
    TypeError: If a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
