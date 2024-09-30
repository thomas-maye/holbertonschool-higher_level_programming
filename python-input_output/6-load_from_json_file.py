#!/usr/bin/python3
"""Module that creates an Object from a "JSON file"."""
import json as j


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".

    Args:
        filename (str): The file to create the object from.

    Returns:
        obj: The object created from the JSON file."""
    with open(filename, mode='r', encoding='utf-8') as f:
        return j.load(f)
