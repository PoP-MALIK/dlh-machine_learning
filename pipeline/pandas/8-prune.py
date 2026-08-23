#!/usr/bin/env python3
"""Removes entries where Close has NaN values."""


def prune(df):
    """Removes rows where Close is NaN.

    Args:
        df (pd.DataFrame): DataFrame to prune

    Returns:
        pd.DataFrame: modified DataFrame
    """
    return df.dropna(subset=['Close'])
