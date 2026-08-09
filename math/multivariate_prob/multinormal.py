#!/usr/bin/env python3
"""Module that defines the MultiNormal distribution class."""
import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize MultiNormal with a data set.

        Args:
            data (numpy.ndarray): shape (d, n) containing the data set
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError('data must be a 2D numpy.ndarray')
        d, n = data.shape
        if n < 2:
            raise ValueError('data must contain multiple data points')

        self.mean = np.sum(data, axis=1, keepdims=True) / n
        deviation = data - self.mean
        self.cov = (deviation @ deviation.T) / (n - 1)
