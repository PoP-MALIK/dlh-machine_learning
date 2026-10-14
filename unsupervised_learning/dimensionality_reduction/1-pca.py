#!/usr/bin/env python3
"""Module that performs PCA on a dataset (fixed number of dimensions)."""
import numpy as np


def pca(X, ndim):
    """Perform PCA on a dataset and return the transformed data.

    Args:
        X (numpy.ndarray): shape (n, d) — n data points, d dimensions.
        ndim (int): new dimensionality of the transformed X.

    Returns:
        numpy.ndarray: T of shape (n, ndim), the transformed version of X.
    """
    X_m = X - np.mean(X, axis=0)
    _, _, Vt = np.linalg.svd(X_m)
    W = Vt[:ndim].T
    return np.matmul(X_m, W)
