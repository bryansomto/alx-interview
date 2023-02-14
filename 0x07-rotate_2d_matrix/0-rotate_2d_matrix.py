#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate a 2D matrix by 90 degrees.
    """
    matrix = list(reversed(matrix))
    return matrix
