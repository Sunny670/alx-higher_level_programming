#!/usr/bin/python3
# 9-rectangle.py
"""Contains a subclass Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Importing function from task 7"""

class Rectangle(BaseGeometry):
    """A representation of a rectangle."""

    def __init__(self, width, height):
        """New Rectangle is initialized."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns  representation of Rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height) 