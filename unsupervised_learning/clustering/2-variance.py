#!/usr/bin/env python3
"""Calculates the total intra-cluster variance for a data set."""
import numpy as np


def variance(X, C):
    """Calculates the total intra-cluster variance for a data set."""
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None
    if not isinstance(C, np.ndarray) or C.ndim != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None
    try:
        dist = np.linalg.norm(X[:, None] - C, axis=2)
        return np.sum(dist.min(axis=1) ** 2)
    except Exception:
        return None
