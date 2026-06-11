#!/usr/bin/env python3
"""Module that defines a function to perform matrix multiplication."""
import numpy as np


def np_matmul(mat1, mat2):
    """Perform matrix multiplication on two numpy matrices.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return np.matmul(mat1, mat2)
