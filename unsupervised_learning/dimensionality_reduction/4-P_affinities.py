#!/usr/bin/env python3
"""Module that calculates the symmetric P affinities of a dataset."""
import numpy as np
P_init = __import__('2-P_init').P_init
HP = __import__('3-entropy').HP


def P_affinities(X, tol=1e-5, perplexity=30.0):
    """Calculate the symmetric P affinities of a dataset.

    Args:
        X (numpy.ndarray): shape (n, d) — dataset to be transformed by t-SNE.
        tol (float): maximum tolerance for the difference in Shannon entropy
            from perplexity for all Gaussian distributions.
        perplexity (float): perplexity that all Gaussian distributions
            should have.

    Returns:
        numpy.ndarray: P of shape (n, n) containing the symmetric P
            affinities.
    """
    n = X.shape[0]
    D, P, betas, H = P_init(X, perplexity)

    for i in range(n):
        Di = np.concatenate((D[i, :i], D[i, i + 1:]))
        beta = betas[i]
        low = None
        high = None

        Hi, Pi = HP(Di, beta)

        while np.abs(Hi - H) > tol:
            if Hi > H:
                low = beta
                beta = beta * 2 if high is None else (beta + high) / 2
            else:
                high = beta
                beta = beta / 2 if low is None else (beta + low) / 2
            Hi, Pi = HP(Di, beta)

        betas[i] = beta
        P[i, :i] = Pi[:i]
        P[i, i + 1:] = Pi[i:]

    P = (P + P.T) / (2 * n)
    return P
