#!/usr/bin/env python3
"""Fills missing values in a pd.DataFrame."""


def fill(df):
    """Fills missing values following column-specific rules.

    Args:
        df (pd.DataFrame): DataFrame to fill

    Returns:
        pd.DataFrame: modified DataFrame
    """
    df = df.drop(columns=['Weighted_Price'])
    df['Close'] = df['Close'].ffill()
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])
    df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
    df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)
    return df
