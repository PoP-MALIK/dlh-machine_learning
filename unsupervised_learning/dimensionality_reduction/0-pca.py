#!/usr/bin/env python3
"""Module that performs PCA on a dataset."""
import numpy as np


def pca(X, var=0.95):
    """Perform PCA on a dataset.

    Args:
        X (numpy.ndarray): shape (n, d) — n data points, d dimensions.
            All dimensions have a mean of 0 across all data points.
        var (float): fraction of variance the transformation must maintain.

    Returns:
        numpy.ndarray: weights matrix W of shape (d, nd) where nd is the
            new dimensionality that maintains var fraction of variance.
    """
    _, s, Vt = np.linalg.svd(X)
    cumvar = np.cumsum(s ** 2) / np.sum(s ** 2)
    nd = np.argmax(cumvar >= var) + 1
    return Vt[:nd].T
