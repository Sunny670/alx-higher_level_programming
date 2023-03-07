#!/usr/bin/python3
def islower(a):
    "Function checks for lowercase characters."
    if ord(a) >= 97 and ord(a) <= 122:
        return True
    else:
        return False
