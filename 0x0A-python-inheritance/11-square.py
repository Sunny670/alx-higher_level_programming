#!/usr/bin/python3
# 11-square.py
"""Contains  a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle
"""Function is imported from task 9."""


class Square(Rectangle):
    """Function that represents a square."""

    def __init__(self, size):
        """New square is initialized."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the square."""
        return self.__size ** 2

    def __str__(self):
        """string representation of square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
