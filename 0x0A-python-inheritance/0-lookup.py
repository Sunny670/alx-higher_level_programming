#!/usr/bin/python3
# 0-lookup.py
"""Defines a lookup function."""


def lookup(obj):
    """Return a list of  objects that are  available attributes."""
    return (dir(obj))
