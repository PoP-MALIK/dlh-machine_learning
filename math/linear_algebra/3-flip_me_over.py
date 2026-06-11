#!/usr/bin/env python3
""" Module that transposes a 2D matrix."""


def matrix_transpose(matrix):
    """Return tthe transpose of a 2D matrix."""
    traspose_matrix = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[col])
        traspose_matrix.append(new_row)
    return traspose_matrix
