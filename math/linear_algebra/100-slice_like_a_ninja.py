#!/usr/bin/env python3
"""Module that slices a matrix along specific axes"""


def np_slice(matrix, axes={}):
    """Slice a NumPy ndarray  along a specific axes"""
    new_matrix = []
    slices = [slice(None)] * matrix.ndim
    for keys, values in axes.items():
        slices[keys] = slice(*values)
    new_matrix = matrix[tuple(slices)]
    return new_matrix
