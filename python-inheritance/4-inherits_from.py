#!/usr/bin/python3
"""A function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified class
otherwise False"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is an instance of a_class
        False otherwise cases
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
