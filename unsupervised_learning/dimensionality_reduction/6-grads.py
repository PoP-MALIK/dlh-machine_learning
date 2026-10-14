#!/usr/bin/env python3
"""Module that calculates the gradients of Y for t-SNE."""
import numpy as np
Q_affinities = __import__('5-Q_affinities').Q_affinities


def grads(Y, P):
    """Calculate the gradients of Y.

    Args:
        Y (numpy.ndarray): shape (n, ndim) — low dimensional transformation
            of X.
        P (numpy.ndarray): shape (n, n) — P affinities of X.

    Returns:
        tuple: (dY, Q)
            dY (numpy.ndarray): shape (n, ndim) gradients of Y.
            Q (numpy.ndarray): shape (n, n) Q affinities of Y.
    """
    Q, num = Q_affinities(Y)
    n, ndim = Y.shape
    PQ = (P - Q) * num
    dY = np.zeros((n, ndim))
    for i in range(n):
        dY[i] = np.sum((PQ[:, i] + PQ[i, :])[:, np.newaxis] *
                       (Y[i] - Y), axis=0)
    return dY, Q
