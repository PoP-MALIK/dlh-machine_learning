#!/usr/bin/env python3
"""Finds the best number of clusters for a GMM using the BIC."""
import numpy as np

expectation_maximization = __import__('8-EM').expectation_maximization


def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """Finds the best number of clusters for a GMM using the BIC."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None
    n, d = X.shape
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None, None, None
    if kmax is None:
        kmax = n
    if not isinstance(kmax, int) or kmax <= 0 or kmax < kmin:
        return None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None
    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None

    logs = []
    bics = []
    results = []
    for k in range(kmin, kmax + 1):
        pi, m, S, g, likelihood = expectation_maximization(
            X, k, iterations, tol, verbose)
        p = (k * d * (d + 1) / 2) + (d * k) + (k - 1)
        bic = p * np.log(n) - 2 * likelihood
        logs.append(likelihood)
        bics.append(bic)
        results.append((pi, m, S))
    logs = np.array(logs)
    bics = np.array(bics)
    best = np.argmin(bics)
    return best + kmin, results[best], logs, bics
