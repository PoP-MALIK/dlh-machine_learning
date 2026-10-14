#!/usr/bin/env python3
"""Module that calculates the cost of the t-SNE transformation."""
import numpy as np


def cost(P, Q):
    """Calculate the cost of the t-SNE transformation (KL divergence).

    Args:
        P (numpy.ndarray): shape (n, n) — P affinities.
        Q (numpy.ndarray): shape (n, n) — Q affinities.

    Returns:
        float: C, the cost of the transformation.
    """
    P = np.maximum(P, 1e-12)
    Q = np.maximum(Q, 1e-12)
    return np.sum(P * np.log(P / Q))
