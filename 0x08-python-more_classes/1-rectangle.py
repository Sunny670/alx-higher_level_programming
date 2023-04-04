#!/usr/bin/python3
# 1-rectangle.py
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the width and height of the
            rectangle with default values of 0.
        Arguments:
            width (int):  Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for the width property
            Check that the input value is an integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """Check that the input value is greater than or equal to 0"""
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        """Check that the input value is greater than or equal to 0"""

    @property
    def height(self):
        """Getter method for the height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height property
           Check that the input value is an integer"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """Check that the input value is greater than or equal to 0"""
        if value < 0:
            raise ValueError("height must be >= 0")
        """ Set the value of the height attribute to the input value"""
        self.__height = value