#!/usr/bin/env python3
"""Module that defines a function to concatenate two numpy matrices."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.
        axis (int): Axis along which to concatenate. Defaults to 0.

    Returns:
        numpy.ndarray: The concatenated matrix.
    """
    return np.concatenate((mat1, mat2), axis=axis)
