#!/usr/bin/env python3
"""Sorts a pd.DataFrame by High price in descending order."""


def high(df):
    """Sorts the DataFrame by High price in descending order.

    Args:
        df (pd.DataFrame): DataFrame to sort

    Returns:
        pd.DataFrame: sorted DataFrame
    """
    return df.sort_values(by='High', ascending=False)
