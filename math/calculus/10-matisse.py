#!/usr/bin/env python3
"""module calculates the derivative of a polynomial"""

def poly_derivative(poly):
    """calculates the derivative of a polynomial"""
    if not isinstance(poly, list) or len(poly) == 0:
        return  None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 1:
        return [0]
    result = [i * poly[i] fot i in range(1, len(poly))]
    if all(c == 0 for c in result):
        return [0]
    return result
