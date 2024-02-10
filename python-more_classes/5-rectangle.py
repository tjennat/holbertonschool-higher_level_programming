#!/usr/bin/python3
"""
module of my rectangle
"""


class Rectangle:
    """
    class of my rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of my rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """This property sets the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """the height of my rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """This property sets the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """string representation of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """string representation of rectangle by using by using eval."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete the instance of rectangle."""
        print("Bye rectangle...")
