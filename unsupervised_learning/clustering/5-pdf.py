#!/usr/bin/env python3
"""Calculates the PDF of a Gaussian distribution."""
import numpy as np


def pdf(X, m, S):
    """Calculates the probability density function of a Gaussian."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(m, np.ndarray) or m.ndim != 1:
        return None
    if not isinstance(S, np.ndarray) or S.ndim != 2:
        return None
    d = X.shape[1]
    if m.shape[0] != d or S.shape[0] != d or S.shape[1] != d:
        return None

    det = np.linalg.det(S)
    inv = np.linalg.inv(S)
    diff = X - m
    exponent = -0.5 * np.sum((diff @ inv) * diff, axis=1)
    norm = 1 / np.sqrt(((2 * np.pi) ** d) * det)
    P = norm * np.exp(exponent)
    return np.maximum(P, 1e-300)
