#!/usr/bin/env python3
"""Renames Timestamp column and converts to datetime."""
import pandas as pd


def rename(df):
    """Renames Timestamp to Datetime, converts values, returns Datetime and Close.

    Args:
        df (pd.DataFrame): DataFrame containing a Timestamp column

    Returns:
        pd.DataFrame: modified DataFrame with Datetime and Close columns
    """
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    return df[['Datetime', 'Close']]
