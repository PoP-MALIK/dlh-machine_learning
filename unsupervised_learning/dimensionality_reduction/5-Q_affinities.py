#!/usr/bin/env python3
"""Module that calculates the Q affinities for t-SNE."""
import numpy as np


def Q_affinities(Y):
    """Calculate the Q affinities.

    Args:
        Y (numpy.ndarray): shape (n, ndim) — low dimensional transformation
            of X.

    Returns:
        tuple: (Q, num)
            Q (numpy.ndarray): shape (n, n) containing the Q affinities.
            num (numpy.ndarray): shape (n, n) numerator of the Q affinities.
    """
    sum_sq = np.sum(Y ** 2, axis=1)
    D = sum_sq[:, np.newaxis] + sum_sq[np.newaxis, :] - 2 * np.matmul(Y, Y.T)
    num = 1 / (1 + D)
    np.fill_diagonal(num, 0)
    Q = num / np.sum(num)
    return Q, num
