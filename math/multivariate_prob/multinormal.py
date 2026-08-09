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

    def pdf(self, x):
        """Calculates the PDF at a data point.

        Args:
            x (numpy.ndarray): shape (d, 1) containing the data point

        Returns:
            float: value of the PDF at x
        """
        if not isinstance(x, np.ndarray):
            raise TypeError('x must be a numpy.ndarray')
        d = self.mean.shape[0]
        if x.shape != (d, 1):
            raise ValueError('x must have the shape ({}, 1)'.format(d))

        pi = 3.1415926536
        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        coefficient = 1 / np.sqrt(((2 * pi) ** d) * det)
        diff = x - self.mean
        exponent = -0.5 * (diff.T @ inv @ diff)
        return float(coefficient * np.exp(exponent))
