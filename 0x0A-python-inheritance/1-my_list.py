#!/usr/bin/python3
# 1-my_list.py
"""Defines  inherited  MyList class."""


class MyList(list):
    """subclass list."""
    def __init__(self):
        """object being initialized"""
        super().__init_()
        
    def print_sorted(self):
        """Prints sorted ascending order list."""
        print(sorted(self))
