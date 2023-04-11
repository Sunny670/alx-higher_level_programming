#!/usr/bin/python3
# 4-inherits_from.py
"""Has an inherited_from class-checking function."""


def inherits_from(obj, a_class):
    """Returns true if obj is subclass to a_class,else False."""

    return(issubclass(type(obj), a_class) and type(obj) != a_class)
