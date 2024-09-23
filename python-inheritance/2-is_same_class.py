#!/usr/bin/python3
"""A function that returns True if the object is
exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance
    of the specified class
    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is exactly an instance of a_class
        False otherwise cases
    """
    if type(obj) is a_class:
        return True
    return False
