#!/usr/bin/python3
"""Module that returns an object (Python data structure)
repesented by a JSON string."""
import json as j


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string to represent.

    Returns:
        obj: The object represented by the JSON string.
    """
    return j.loads(my_str)
