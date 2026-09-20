#!/usr/bin/env python3
"""Performs agglomerative clustering on a dataset."""
import scipy.cluster.hierarchy
import matplotlib.pyplot as plt


def agglomerative(X, dist):
    """Performs agglomerative clustering with Ward linkage.

    Displays the dendrogram with each cluster in a different color.
    Returns clss, a numpy.ndarray of shape (n,) containing the
    cluster indices for each data point.
    """
    Z = scipy.cluster.hierarchy.linkage(X, method='ward')
    clss = scipy.cluster.hierarchy.fcluster(Z, t=dist, criterion='distance')
    scipy.cluster.hierarchy.dendrogram(Z, color_threshold=dist)
    plt.show()
    return clss
