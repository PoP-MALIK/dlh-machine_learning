#!/usr/bin/env python3
"""Slices a pd.DataFrame to extract specific columns every 60th row."""
import pandas as pd


def slice(df):
    """Extracts High, Low, Close, Volume_(BTC) columns every 60th row.

    Args:
        df (pd.DataFrame): DataFrame to slice

    Returns:
        pd.DataFrame: sliced DataFrame
    """
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
