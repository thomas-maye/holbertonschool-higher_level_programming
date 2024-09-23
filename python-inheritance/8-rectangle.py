#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle based on 7-base_geometry.py"""

    def __init__(self, width, height):
        """Initializes a Rectangle object
        Args:
            width: integer
            height: integer
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
