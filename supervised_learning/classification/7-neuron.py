#!/usr/bin/env python3
"""Defines a single neuron performing binary classification."""
import matplotlib.pyplot as plt
import numpy as np


class Neuron:
    """A single neuron performing binary classification."""

    def __init__(self, nx):
        """Initialize the neuron.

        Args:
            nx: Number of input features.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Return the weights vector."""
        return self.__W

    @property
    def b(self):
        """Return the bias."""
        return self.__b

    @property
    def A(self):
        """Return the activated output."""
        return self.__A

    def forward_prop(self, X):
        """Calculate the forward propagation of the neuron.

        Args:
            X: numpy.ndarray of shape (nx, m) with the input data.

        Returns:
            The activated output (sigmoid), also stored in __A.
        """
        Z = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """Calculate the cost using logistic regression.

        Args:
            Y: numpy.ndarray of shape (1, m) with the correct labels.
            A: numpy.ndarray of shape (1, m) with the activated output.

        Returns:
            The cost.
        """
        m = Y.shape[1]
        loss = Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        return -np.sum(loss) / m

    def evaluate(self, X, Y):
        """Evaluate the neuron's predictions.

        Args:
            X: numpy.ndarray of shape (nx, m) with the input data.
            Y: numpy.ndarray of shape (1, m) with the correct labels.

        Returns:
            The predicted labels (1 if A >= 0.5, else 0) and the cost.
        """
        A = self.forward_prop(X)
        prediction = np.where(A >= 0.5, 1, 0)
        return prediction, self.cost(Y, A)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """Calculate one pass of gradient descent on the neuron.

        Args:
            X: numpy.ndarray of shape (nx, m) with the input data.
            Y: numpy.ndarray of shape (1, m) with the correct labels.
            A: numpy.ndarray of shape (1, m) with the activated output.
            alpha: The learning rate.
        """
        m = Y.shape[1]
        dz = A - Y
        dW = np.matmul(dz, X.T) / m
        db = np.sum(dz) / m
        self.__W = self.__W - alpha * dW
        self.__b = self.__b - alpha * db

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """Train the neuron.

        Args:
            X: numpy.ndarray of shape (nx, m) with the input data.
            Y: numpy.ndarray of shape (1, m) with the correct labels.
            iterations: Number of iterations to train over.
            alpha: The learning rate.
            verbose: Whether to print the cost every step iterations.
            graph: Whether to plot the cost once training is done.
            step: Number of iterations between prints and plot points.

        Returns:
            The evaluation of the training data after training.
        """
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        if verbose or graph:
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if step <= 0 or step > iterations:
                raise ValueError("step must be positive and <= iterations")

        steps = []
        costs = []
        for i in range(iterations + 1):
            A = self.forward_prop(X)
            if (verbose or graph) and (i % step == 0 or i == iterations):
                cost = self.cost(Y, A)
                steps.append(i)
                costs.append(cost)
                if verbose:
                    print("Cost after {} iterations: {}".format(i, cost))
            if i < iterations:
                self.gradient_descent(X, Y, A, alpha)

        if graph:
            plt.plot(steps, costs, 'b')
            plt.xlabel("iteration")
            plt.ylabel("cost")
            plt.title("Training Cost")
            plt.show()
        return self.evaluate(X, Y)
