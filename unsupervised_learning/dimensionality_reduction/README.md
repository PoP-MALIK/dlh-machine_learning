# Dimensionality Reduction

This project implements PCA and t-SNE from scratch using NumPy.

## Files

| File | Description |
|------|-------------|
| `0-pca.py` | PCA — weight matrix maintaining a given fraction of variance |
| `1-pca.py` | PCA v2 — centers data and projects to fixed number of dimensions |
| `2-P_init.py` | Initializes t-SNE variables: D, P, betas, H |
| `3-entropy.py` | Shannon entropy and P affinities for a single point |
| `4-P_affinities.py` | Symmetric P affinities via binary search on beta |
| `5-Q_affinities.py` | Q affinities using Student t-distribution kernel |
| `6-grads.py` | Gradients of Y with respect to KL divergence cost |
| `7-cost.py` | KL divergence cost between P and Q |
| `8-tsne.py` | Full t-SNE: PCA reduction, P affinities, gradient descent |

## Requirements

- Python 3.9
- NumPy 1.25.2

## Concepts

### PCA
Linear dimensionality reduction via SVD. Finds orthogonal axes of maximum variance.

### t-SNE
Non-linear dimensionality reduction. Minimizes KL divergence between high-D Gaussian similarities (P) and low-D Student t-distribution similarities (Q) via gradient descent with momentum and early exaggeration.
