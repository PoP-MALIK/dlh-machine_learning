#!/usr/bin/env python3
"""Module for Poisson distribution"""


class Poisson:
    """Represents a Poisson distribution

    Attributes:
        lambtha (float): Expected number of occurrences in a given
            time frame
    """

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Initializes a Poisson distribution

        Args:
            data (list): Data to estimate the distribution from
            lambtha (float): Expected number of occurrences in a given
                time frame

        Raises:
            ValueError: If lambtha is not a positive value
            TypeError: If data is not a list
            ValueError: If data does not contain multiple values
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the PMF value for a given number of successes

        Args:
            k (int): Number of successes

        Returns:
            float: PMF value for k, or 0 if k is out of range
        """
        k = int(k)
        if k < 0:
            return 0
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        return (self.e ** -self.lambtha) * (self.lambtha ** k) / factorial

    def cdf(self, k):
        """Calculates the CDF value for a given number of successes

        Args:
            k (int): Number of successes

        Returns:
            float: CDF value for k, or 0 if k is out of range
        """
        k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(i) for i in range(k + 1))
