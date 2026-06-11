#!/usr/bin/env python3
"""Module that defines a function for element-wise numpy operations."""
import numpy as np


def np_elementwise(mat1, mat2):
    """Perform element-wise addition, subtraction, multiplication, division.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix or scalar.

    Returns:
        tuple: (sum, difference, product, quotient)
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
