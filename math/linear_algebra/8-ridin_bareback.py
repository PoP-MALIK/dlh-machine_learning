#!/usr/bin/env python3
"""Module that performs matrix multiplication:."""


def mat_mul(mat1, mat2):
    """Returns the peforms of a matrix multiplicatio"""
    if len(mat1[0]) != len(mat2):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2[0])):
            multiplication = 0
            for k in range(len(mat2)):
                multiplication += (mat1[i][k] * mat2[k][j])
            new_row.append(multiplication)
        new_matrix.append(new_row)
    return new_matrix
