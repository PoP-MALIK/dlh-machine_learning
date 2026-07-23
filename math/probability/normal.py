#!/usr/bin/env python3
"""Module for Normal distribution"""


class Normal:
    """Represents a Normal distribution

    Attributes:
        mean (float): Mean of the distribution
        stddev (float): Standard deviation of the distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes a Normal distribution

        Args:
            data (list): Data to estimate the distribution from
            mean (float): Mean of the distribution
            stddev (float): Standard deviation of the distribution

        Raises:
            ValueError: If stddev is not a positive value
            TypeError: If data is not a list
            ValueError: If data does not contain multiple values
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x value

        Args:
            x (float): x value

        Returns:
            float: z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x value of a given z-score

        Args:
            z (float): z-score

        Returns:
            float: x value of z
        """
        return (z * self.stddev) + self.mean
