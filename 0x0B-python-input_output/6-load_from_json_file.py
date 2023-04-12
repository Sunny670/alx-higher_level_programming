#!/usr/bin/python3
# 6-load_from_json_file.py
"""
contains a function that creates an Object from the “JSON file”
"""

import json


def load_from_json_file(filename):
    """creates an object using the "JSON file" """
    with open(filename) as f:
        return json.load(f)