#!/usr/bin/env python3
"""Serialize and deserialize using the XML as ann alternative
format to JSON."""
import xml.etree.ElementTree as ET
import json as j


def serialize_to_xml(data, filename):
    """Serialize the dictionary to an XML file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The file path to save the XML file.
    """
    root = ET.Element("data")
    for key, value in data.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize the XML file to a Python dictionary.

    Args:
        filename (str): The file path to load the XML file.

    Returns:
        dict: The Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data


def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
        }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)


if __name__ == "__main__":
    main()
