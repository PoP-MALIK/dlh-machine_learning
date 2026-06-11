#!/usr/bin/env python3
"""Module that defines a function to add two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Add two arrays element-wise and return a new list.

    Args:
        arr1 (list): First list of ints/floats.
        arr2 (list): Second list of ints/floats.

    Returns:
        list: Element-wise sum, or None if shapes differ.
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
