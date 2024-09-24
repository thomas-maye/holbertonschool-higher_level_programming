#!/usr/bin/env python3
"""Shapes Interfaces and Duck Typing."""

import math
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Create Shape abstract class."""
    @abstractmethod
    def area(self):
        """Create an area abstract method."""
        pass

    @abstractmethod
    def perimeter(self):
        """Create a perimeter abstract method."""
        pass


class Circle(Shape):
    """Create a Circle class."""
    def __init__(self, radius):
        """Create a constructor for Circle class."""
        self.radius = radius

    def area(self):
        """Create an area method for Circle class.

        Returns:
            int: pi * self.radius ** 2
        """
        return pi * self.radius ** 2

    def perimeter(self):
        """Create a perimeter method for Circle class.

        Returns:
            int: 2 * pi * self.radius
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Create a Recatngle class."""
    def __init__(self, width, height):
        """Create a constructor for Rectangle class."""
        self.width = width
        self.height = height

    def area(self):
        """Create an area method for Rectangle class.

        Returns:
            int: self.width * self.height
        """
        return self.width * self.height

    def perimeter(self):
        """Create a perimeter method for Rectangle class.

        Returns:
            int: 2 * (self.width + self.height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape.

    Args:
        shape (Shape): A shape object.
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
