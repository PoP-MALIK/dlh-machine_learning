#!/usr/bin/env python3
"""Sorts a pd.DataFrame in reverse order and transposes it."""


def flip_switch(df):
    """Sorts data in reverse chronological order and transposes it.

    Args:
        df (pd.DataFrame): DataFrame to transform

    Returns:
        pd.DataFrame: sorted and transposed DataFrame
    """
    return df.sort_index(ascending=False).transpose()
