#!/usr/bin/python3
"""Module that writes an Object to a texte file,
using a JSON representation."""
import json as j


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (obj): The object to write.
        filename (str): The file to write.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(j.dumps(my_obj))
