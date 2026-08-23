#!/usr/bin/env python3
"""Concatenates two pd.DataFrame objects with keys."""
import pandas as pd

index = __import__('10-index').index


def concat(df1, df2):
    """Concatenates selected rows from df2 to the top of df1.

    Args:
        df1 (pd.DataFrame): coinbase DataFrame
        df2 (pd.DataFrame): bitstamp DataFrame

    Returns:
        pd.DataFrame: concatenated DataFrame with keys
    """
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[:1417411920]
    return pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
