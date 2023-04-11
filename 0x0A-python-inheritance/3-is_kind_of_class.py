#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Contains a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """The function returns true if the object is an instance or inherited
       from a_class, else False.
    """
    return (isinstance(obj, a_class))
