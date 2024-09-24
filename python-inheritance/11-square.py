#!/usr/bin/python3
"""A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
(task based on 8-rectangle.py)."""


class BaseGeometry:
    """A class BaseGeometry based on 6-base_geometry.py"""

    def area(self):
        """Raises an Exception with the message area() is not implemented

        Raises:
            Exception: with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name: string
            value: integer

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class Rectangle based on 7-base_geometry.py"""

    def __init__(self, width, height):
        """Initializes a Rectangle object

        Args:
            width: integer
            height: integer

        Raises:
            Without
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates the area of a Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of a Rectangle object

        Returns:
            string: [Rectangle] {}/{}
        """
        return "[{}] {}/{}".format(
            self.__class__.__name__, self.__width, self.__height)


class Square(Rectangle):
    """A class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Initializes a Rectangle object

        Args:
            width: integer
            height: integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
