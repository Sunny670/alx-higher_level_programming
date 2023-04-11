#!/usr/bin/python3
# 10-square.py
"""Contains Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle
"""Function imported from task 9."""


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """New square is initialized."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of square"""
        return self.__size ** 2
