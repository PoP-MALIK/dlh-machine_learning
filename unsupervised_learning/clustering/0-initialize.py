#!/usr/bin/env python3
"""Initializes cluster centroids for K-means."""
import numpy as np


def initialize(X, k):
    """Initializes cluster centroids for K-means.

    X is a numpy.ndarray of shape (n, d) containing the dataset.
    k is a positive integer, the number of clusters.

    Returns a numpy.ndarray of shape (k, d) with the initialized
    centroids, or None on failure.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(k, int) or k <= 0:
        return None
    _, d = X.shape
    low = X.min(axis=0)
    high = X.max(axis=0)
    return np.random.uniform(low, high, size=(k, d))
