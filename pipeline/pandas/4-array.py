#!/usr/bin/env python3
"""Converts last 10 rows of High and Close columns to numpy.ndarray."""


def array(df):
    """Selects last 10 rows of High and Close and converts to ndarray.

    Args:
        df (pd.DataFrame): DataFrame containing High and Close columns

    Returns:
        numpy.ndarray: last 10 rows of High and Close
    """
    return df[['High', 'Close']].tail(10).to_numpy()
