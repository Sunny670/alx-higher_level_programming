#!/usr/bin/python3

# Defines an integer addition function.


def add_integer(a, b=98):
    """
    This function takes two arguments, a and b, and returns their sum as an integer.
    If a or b is not an integer or a float, it raises a TypeError.
    If a or b is a float, it is cast to an integer before the addition.
    If b is not provided, it defaults to 98.
    """
    
    # Check if a is an integer or float, raise TypeError if not
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    
    # Check if b is an integer or float, raise TypeError if not
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    
    # Cast a to an integer if it is a float
    a = int(a)
    
    # Cast b to an integer if it is a float
    b = int(b)
    
    # Return the sum of a and b as an integer
    return a + b