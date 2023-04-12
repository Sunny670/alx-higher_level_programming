#!/usr/bin/python3
# 12-pascal_triangle.p
"""Contains a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size y.
    Returns list of lists of integers that represents a triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        last_row = triangles[-1]
        new_row = [1]
        for index in range(len(last_row) - 1):
            new_row.append(last_row[index] + last_row[index + 1])
        new_row.append(1)
        triangles.append(new_row)
    return triangles