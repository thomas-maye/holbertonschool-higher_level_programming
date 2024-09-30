#!/usr/bin/env python3
"""Create a basic serialization module that adds the
functionality to serialize a Python dictionary to a JSON
file and deserialize the JSON file to recreate the Python
Dictionary."""
import json as j


def serialize_dict_to_json_file(data, filename):
    """Serialize the dictionary to a JSON file.

    Args:
        dictionary (dict): The dictionary to serialize.
        file_path (str): The file path to save the JSON file.
    """
    with open(filename, 'w') as file:
        j.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a Python dictionary.

    Args:
        file_path (str): The file path to load the JSON file.
    """
    with open(filename, 'r') as file:
        return j.load(file)


if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_dict_to_json_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
