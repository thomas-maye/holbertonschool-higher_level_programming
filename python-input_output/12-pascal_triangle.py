#!/usr/bin/python3
"""Pascal's Triangle a function that returns a list of lists
of integers representing the Pascal's triangle of a given number
of rows."""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal's triangle of a given number of rows."""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
