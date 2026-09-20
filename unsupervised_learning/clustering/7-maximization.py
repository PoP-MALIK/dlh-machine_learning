#!/usr/bin/env python3
"""Calculates the maximization step in the EM algorithm for a GMM."""
import numpy as np


def maximization(X, g):
    """Calculates the maximization step in the EM algorithm for a GMM."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or g.ndim != 2:
        return None, None, None
    n, d = X.shape
    k = g.shape[0]
    if g.shape[1] != n:
        return None, None, None
    if not np.allclose(np.sum(g, axis=0), 1):
        return None, None, None

    Nk = np.sum(g, axis=1)
    pi = Nk / n
    m = (g @ X) / Nk[:, None]
    S = np.zeros((k, d, d))
    for i in range(k):
        diff = X - m[i]
        S[i] = (g[i] * diff.T) @ diff / Nk[i]
    return pi, m, S
