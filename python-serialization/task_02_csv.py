#!/usr/bin/env python3
"""Read a CSV data file and converting it into an another format (JSON)."""
import csv
import json as j


def convert_csv_to_json(csv_filename):
    """Convert the CSV data to JSON format.

    Args:
        csv_filename (str): The CSV file path.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as file:
            csv_data = list(csv.DictReader(file))
        with open('data.json', 'w') as json_file:
                j.dump(csv_data, json_file)
        return True
    except (FileNotFoundError, Exception):
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
