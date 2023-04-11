#!/usr/bin/python3
# 100-my_int.py
"""Contains the class MyInt that inherits from int."""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, other):
        """Switches == opeartor with != action."""
        return int(self) != other

    def __ne__(self, other):
        """switches != operator with == action."""
        return int(self) == other
