#!/usr/bin/python3
# 8-rectangle.py
"""Contains a subclass Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle ."""

    def __init__(self, width, height):
        """New Rectangle is initialized."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height 
