#!/usr/bin/python3
"""A function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class
    Args:
        obj: object
        a_class: class
    Returns:
        True if obj is an instance of a_class
        False otherwise cases
    """
    if isinstance(obj, a_class):
        return True
    return False
