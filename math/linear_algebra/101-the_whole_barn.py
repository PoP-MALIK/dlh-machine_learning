#!/usr/bin/env python3
"""Module that adds two matrices"""


def add_matrices(mat1, mat2):
    """Returns the addition of matrices"""
    if not isinstance(mat1, list):
        return mat1 + mat2
    if len(mat1) != len(mat2):
        return None
    else:
        sum_total = 0
        new_matrix = []
        for i in range(len(mat1)):
            sum_total = add_matrices(mat1[i], mat2[i])
            if sum_total is None:
                return None
            new_matrix.append(sum_total)
    return new_matrix
