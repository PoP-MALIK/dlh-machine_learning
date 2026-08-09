#!/usr/bin/env python3
"""Calculates the mean and covariance of a data set."""
import numpy as np


def mean_cov(X):
    """Calculates the mean and covariance of a data set.

    Args:
        X (numpy.ndarray): shape (n, d) containing the data set

    Returns:
        tuple: (mean, cov)
            mean is a numpy.ndarray of shape (1, d)
            cov is a numpy.ndarray of shape (d, d)
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError('X must be a 2D numpy.ndarray')
    n, d = X.shape
    if n < 2:
        raise ValueError('X must contain multiple data points')

    mean = np.sum(X, axis=0, keepdims=True) / n
    deviation = X - mean
    cov = (deviation.T @ deviation) / (n - 1)
    return mean, cov
