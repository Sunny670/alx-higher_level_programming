#!/usr/bin/python3
# 5-save_to_json_file.py
"""
contains a function that writes an Object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes  object to a text file, using  JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
