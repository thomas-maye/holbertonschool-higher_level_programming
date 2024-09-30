#!/usr/bin/python3
"""Module to write an object to a text file using
JSON representation of an objetc."""
import json as j


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj (obj): The object to represent.

    Returns:
        str: The JSON representation of the object.
    """
    return j.dumps(my_obj)
