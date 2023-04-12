#!/usr/bin/python3
# 0-read_file.py
"""
Contains a function named read_file."""


def read_file(filename=""):
    """""reads  text file(UTF8) and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
