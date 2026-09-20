# Clustering

Unsupervised learning project implementing K-means and Gaussian Mixture Models (GMM)
from scratch with numpy, plus the Expectation-Maximization (EM) algorithm, the
Bayesian Information Criterion (BIC) for model selection, and scikit-learn equivalents.

## Requirements

- Ubuntu 20.04 LTS, python3 (3.9)
- numpy 1.25.2, scikit-learn 1.5.0, scipy 1.11.4
- Style: pycodestyle 2.11.1
- All files are executable and start with #!/usr/bin/env python3
- Every module, class, and function is documented

## Files

- 0-initialize.py: initialize(X, k) — K-means centroid initialization
- 1-kmeans.py: kmeans(X, k, iterations=1000) — full K-means
- 2-variance.py: variance(X, C) — total intra-cluster variance
- 4-initialize.py: initialize(X, k) — GMM variable initialization
- 5-pdf.py: pdf(X, m, S) — multivariate Gaussian PDF
- 6-expectation.py: expectation(X, pi, m, S) — EM E-step
- 7-maximization.py: maximization(X, g) — EM M-step
- 8-EM.py: expectation_maximization(X, k, ...) — full EM loop
- 9-BIC.py: BIC(X, kmin, kmax, ...) — best cluster count via BIC
- 10-kmeans.py: kmeans(X, k) — sklearn K-means
- 11-gmm.py: gmm(X, k) — sklearn GMM

## Author

Melek Jaffel — PoP-MALIK
