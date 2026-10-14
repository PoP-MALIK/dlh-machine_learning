#!/usr/bin/env python3
"""Module that performs a full t-SNE transformation."""
import numpy as np
pca = __import__('1-pca').pca
P_affinities = __import__('4-P_affinities').P_affinities
grads = __import__('6-grads').grads
cost = __import__('7-cost').cost


def tsne(X, ndims=2, idims=50, perplexity=30.0, iterations=1000, lr=500):
    """Perform a t-SNE transformation.

    Args:
        X (numpy.ndarray): shape (n, d) — dataset to transform.
        ndims (int): new dimensional representation of X.
        idims (int): intermediate dimensions after PCA.
        perplexity (float): perplexity for Gaussian distributions.
        iterations (int): number of gradient descent iterations.
        lr (float): learning rate.

    Returns:
        numpy.ndarray: Y of shape (n, ndims) — optimized low dimensional
            transformation of X.
    """
    n = X.shape[0]
    X = pca(X, idims)
    P = P_affinities(X, perplexity=perplexity)

    np.random.seed(0)
    Y = np.random.randn(n, ndims)
    iY = np.zeros((n, ndims))

    for t in range(1, iterations + 1):
        alpha = 0.5 if t <= 20 else 0.8
        P_use = P * 4 if t <= 100 else P

        dY, Q = grads(Y, P_use)
        iY = alpha * iY - lr * dY
        Y = Y + iY
        Y = Y - np.mean(Y, axis=0)

        if t % 100 == 0:
            C = cost(P, Q)
            print("Cost at iteration {}: {}".format(t, C))

    return Y
