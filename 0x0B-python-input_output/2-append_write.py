#!/usr/bin/python3
# 2-append_write.py
"""
 Contains a function that appends a string
"""


def append_write(filename="", text=""):
    """returns number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
