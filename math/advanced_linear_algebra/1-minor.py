#!/usr/bin/env python3
"""Module for calculating the minor matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix (helper).

    Args:
        matrix: a list of lists

    Returns:
        The determinant of matrix.
    """
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(len(matrix)):
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def minor(matrix):
    """Calculate the minor matrix of a matrix.

    Args:
        matrix: a list of lists whose minor matrix should be calculated

    Returns:
        The minor matrix of matrix.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # 1x1 special case: minor is [[1]] by convention
    if n == 1:
        return [[1]]

    result = []
    for i in range(n):
        row_result = []
        for j in range(n):
            sub = [r[:j] + r[j + 1:] for r in matrix if r is not matrix[i]]
            row_result.append(determinant(sub))
        result.append(row_result)
    return result
