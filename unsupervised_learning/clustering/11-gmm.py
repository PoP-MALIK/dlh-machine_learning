#!/usr/bin/env python3
"""Calculates a GMM from a dataset using sklearn."""
import sklearn.mixture


def gmm(X, k):
    """Calculates a GMM from a dataset using sklearn."""
    model = sklearn.mixture.GaussianMixture(n_components=k).fit(X)
    clss = model.predict(X)
    bic = model.bic(X)
    return model.weights_, model.means_, model.covariances_, clss, bic
