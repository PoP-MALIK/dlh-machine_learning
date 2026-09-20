#!/usr/bin/env python3
"""Performs K-means on a dataset."""
import numpy as np


def kmeans(X, k, iterations=1000):
    """Performs K-means clustering on a dataset."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None
    if not isinstance(k, int) or k <= 0:
        return None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None

    n, d = X.shape
    low = X.min(axis=0)
    high = X.max(axis=0)
    C = np.random.uniform(low, high, size=(k, d))

    for _ in range(iterations):
        dist = np.linalg.norm(X[:, None] - C, axis=2)
        clss = dist.argmin(axis=1)
        new_C = np.copy(C)
        for j in range(k):
            if np.any(clss == j):
                new_C[j] = X[clss == j].mean(axis=0)
            else:
                new_C[j] = np.random.uniform(low, high, size=(d,))
        if np.array_equal(C, new_C):
            break
        C = new_C

    dist = np.linalg.norm(X[:, None] - C, axis=2)
    clss = dist.argmin(axis=1)
    return C, clss
