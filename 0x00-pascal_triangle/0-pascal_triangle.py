#!/usr/bin/python3
"""Pascal Triangle Interview."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # define row and fill fill first and last idx with 1
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for j in range(1, i):
            a = pascal_triangle[i-1][j]
            b = pascal_triangle[i-1][j-1]
            # print(pascal_triangle[i-1])
            # print(pascal_triangle[i-1][j])
            # print(pascal_triangle[i-1][j-1])
            row[j] = a + b

        pascal_triangle[i] = row

    return pascal_triangle
