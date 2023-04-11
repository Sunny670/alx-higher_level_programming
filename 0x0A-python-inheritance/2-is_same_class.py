#!/usr/bin/python3
# 2-is_same_class.py
"""Module has  a function that checks a class (is_same_class)."""


def is_same_class(obj, a_class):
    """returns true if the object is exact class otherwise false."""
    if type(obj) == a_class:
        return True
    return False
