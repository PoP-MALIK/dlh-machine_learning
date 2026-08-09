#!/usr/bin/env python3
"""Calculates the posterior probability for hypothetical probabilities."""
import numpy as np


def posterior(x, n, P, Pr):
    """Calculates the posterior probability of each probability in P.

    Args:
        x (int): number of patients with severe side effects
        n (int): total number of patients observed
        P (numpy.ndarray): 1D array of hypothetical probabilities
        Pr (numpy.ndarray): 1D array of prior beliefs of P

    Returns:
        numpy.ndarray: posterior probability of each probability in P
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')
    if not isinstance(x, int) or x < 0:
        raise ValueError(
            'x must be an integer that is greater than or equal to 0'
        )
    if x > n:
        raise ValueError('x cannot be greater than n')
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError('P must be a 1D numpy.ndarray')
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError('Pr must be a numpy.ndarray with the same shape as P')
    if np.any((P < 0) | (P > 1)):
        raise ValueError('All values in P must be in the range [0, 1]')
    if np.any((Pr < 0) | (Pr > 1)):
        raise ValueError('All values in Pr must be in the range [0, 1]')
    if not np.isclose(Pr.sum(), 1):
        raise ValueError('Pr must sum to 1')

    factorial_n = 1
    for i in range(1, n + 1):
        factorial_n *= i
    factorial_x = 1
    for i in range(1, x + 1):
        factorial_x *= i
    factorial_nx = 1
    for i in range(1, n - x + 1):
        factorial_nx *= i
    coefficient = factorial_n // (factorial_x * factorial_nx)

    like = np.array(coefficient * (P ** x) * ((1 - P) ** (n - x)))
    intersection = like * Pr
    marg = float(np.sum(intersection))
    return intersection / marg
