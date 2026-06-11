#!/usr/bin/env python3
"""Module that concatenates two matrices."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Returns the concaten´stes of two matrices"""
    new_matrix = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        else:
            for row in mat1:
                new_matrix.append(row[:])
            for row in mat2:
                new_matrix.append(row[:])
        return new_matrix
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        else:
            for i in range(len(mat1)):
                new_matrix.append(mat1[i] + mat2[i])
        return new_matrix
