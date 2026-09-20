#!/usr/bin/env python3
"""Performs the expectation maximization for a GMM."""
import numpy as np

initialize = __import__('4-initialize').initialize
expectation = __import__('6-expectation').expectation
maximization = __import__('7-maximization').maximization


def expectation_maximization(X, k, iterations=1000, tol=1e-5, verbose=False):
    """Performs the expectation maximization for a GMM."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None, None
    if not isinstance(k, int) or k <= 0:
        return None, None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None, None
    if not isinstance(tol, float) or tol < 0:
        return None, None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None, None

    pi, m, S = initialize(X, k)
    g, likelihood = expectation(X, pi, m, S)
    prev = 0
    for i in range(iterations):
        if verbose and i % 10 == 0:
            print('Log Likelihood after {} iterations: {}'.format(
                i, round(likelihood, 5)))
        pi, m, S = maximization(X, g)
        g, likelihood = expectation(X, pi, m, S)
        if abs(likelihood - prev) <= tol:
            break
        prev = likelihood
    if verbose:
        print('Log Likelihood after {} iterations: {}'.format(
            i + 1, round(likelihood, 5)))
    return pi, m, S, g, likelihood
