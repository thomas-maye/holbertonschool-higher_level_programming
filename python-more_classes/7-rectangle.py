#!/usr/bin/python3
"""Function that defines a rectangle"""


class Rectangle:
    """Create a class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes width and height of rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width of rectangle
        Returns:
            width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Getter for height of rectangle
        Returns:
            height of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle
        Returns:
            Area of rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of a rectangle
        Returns:
            Perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle with the character #"""
        if self.width == 0 or self.height == 0:
            return ""
        rect_str = ""
        for _ in range(self.height):
            rect_str += str(self.print_symbol) * self.width + "\n"
        return rect_str.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete method for rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
