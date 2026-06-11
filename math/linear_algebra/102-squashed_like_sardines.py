#!/usr/bin/env python3
"""Module that concatenates two matrices along a specific axis"""


def cat_matrices(mat1, mat2, axis=0):
    """Returns the concatenate of two matrices along a specific axis"""
    shape1 = matrix_shape(mat1)
    shape2 = matrix_shape(mat2)
    if len(shape1) != len(shape2) or axis >= len(shape1):
        return None
    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None
    new_matrix = []
    if axis == 0:
        for row in mat1:
            new_matrix.append(row)
        for row in mat2:
            new_matrix.append(row)
        return new_matrix
    else:
        for i in range(len(mat1)):
            result = cat_matrices(mat1[i], mat2[i], axis - 1)
            if result is None:
                return None
            new_matrix.append(result)
        return new_matrix


def matrix_shape(matrix):
    """This function return the shape of a matrix"""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
