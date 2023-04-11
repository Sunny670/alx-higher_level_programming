#!/usr/bin/python3
# 7-base_geometry.py
"""Has a class BaseGeometry."""


class BaseGeometry:
    """Integer_validator class with public instance methods area."""

    def area(self):
        """exception raised when the function is called."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value  as an integer that's larger than .
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
