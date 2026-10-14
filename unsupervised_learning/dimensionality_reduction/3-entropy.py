#!/usr/bin/env python3
"""Module that calculates Shannon entropy and P affinities for a data point."""
import numpy as np


def HP(Di, beta):
    """Calculate the Shannon entropy and P affinities relative to a data point.

    Args:
        Di (numpy.ndarray): shape (n - 1,) pairwise distances between a data
            point and all other points except itself.
        beta (numpy.ndarray): shape (1,) beta value for the Gaussian
            distribution. beta = 1 / (2 * sigma^2).

    Returns:
        tuple: (Hi, Pi)
            Hi (float): Shannon entropy of the points.
            Pi (numpy.ndarray): shape (n - 1,) P affinities of the points.
    """
    Pi = np.exp(-Di * beta)
    sum_Pi = np.sum(Pi)
    Pi = Pi / sum_Pi
    Hi = -np.sum(Pi * np.log2(Pi))
    return Hi, Pi
