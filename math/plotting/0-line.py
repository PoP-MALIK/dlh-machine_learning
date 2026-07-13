#!/usr/bin/env python3
"""Module for plotting a line graph."""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """Plot y as a solid red line graph."""

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    x = np.arange(0, 11)
    plt.plot(x, y, 'r-')
    plt.xlim(0, 10)

    plt.show()
