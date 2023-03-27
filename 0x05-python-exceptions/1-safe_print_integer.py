#!/usr/bin/python3
def sa_print_integer(value):
    """Print an integer with "{:d}".fomart().
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError of Va;ueError occurs -False.
        Otherwise -True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
