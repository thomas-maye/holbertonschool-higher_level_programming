#!/usr/bin/env python3
"""Learn how to serialize and deserialize custom Python
objects using the pickle module."""
import pickle as p
import json as j


class CustomObject:
    """A custom Python object to be serialized and
    deserialized."""
    def __init__(self, name, age, is_student):
        """Initialize the custom object.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): A boolean.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def __str__(self):
        """Return a string representation of the object.

        Returns:
            str: The string representation of the object."""
        return 
        f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}"

    def serialize(self, filename):
        """Serialize the object to a file.

        Args:
            filename (str): The file path to save the serialized object.

        Returns:
            bool: True if the object was successfully serialized.
        """
        try:
            with open(filename, 'wb') as file:
                p.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the object from a file.

        Args:
            filename (str): The file path to load the serialized object.

        Returns:
            CustomObject: An instance of CustomObject if deserialization is
            successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                return p.load(file)
        except Exception:
            return None

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")


if __name__ == "__main__":
    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()
