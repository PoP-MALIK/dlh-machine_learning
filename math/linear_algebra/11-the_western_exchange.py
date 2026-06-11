#!/usr/bin/env python3
"""Module that defines a function to transpose a numpy matrix."""
import numpy as np


def np_transpose(matrix):
    """Transpose a numpy matrix and return a new numpy.ndarray.

    Args:
        matrix (numpy.ndarray): The matrix to transpose.

    Returns:
        numpy.ndarray: The transposed matrix.
    """
    return matrix.T
