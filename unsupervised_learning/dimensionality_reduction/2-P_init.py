#!/usr/bin/env python3
"""Module that initializes variables for t-SNE P affinities."""
import numpy as np


def P_init(X, perplexity):
    """Initialize all variables required to calculate P affinities in t-SNE.

    Args:
        X (numpy.ndarray): shape (n, d) — dataset to be transformed.
        perplexity (float): perplexity that all Gaussian distributions
            should have.

    Returns:
        tuple: (D, P, betas, H)
            D (numpy.ndarray): shape (n, n) squared pairwise distances,
                diagonal is 0.
            P (numpy.ndarray): shape (n, n) initialized to 0s.
            betas (numpy.ndarray): shape (n, 1) initialized to 1s.
            H (float): Shannon entropy for the given perplexity (base 2).
    """
    n = X.shape[0]
    sum_sq = np.sum(X ** 2, axis=1)
    D = sum_sq[:, np.newaxis] + sum_sq[np.newaxis, :] - 2 * np.matmul(X, X.T)
    np.fill_diagonal(D, 0)
    P = np.zeros((n, n))
    betas = np.ones((n, 1))
    H = np.log2(perplexity)
    return D, P, betas, H
