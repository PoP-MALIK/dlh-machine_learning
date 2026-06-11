#!/usr/bin/env python3
"""Module that caculates matrix shape."""


def matrix_shape(matrix):
    """This function return the shape of a matrix"""
    shape_list = []
    while isinstance(matrix, list):
        shape_list.append(len(matrix))
        matrix = matrix[0]
    return shape_list
