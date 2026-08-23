#!/usr/bin/env python3
"""Computes descriptive statistics for all columns except Timestamp."""


def analyze(df):
    """Computes descriptive statistics excluding the Timestamp column.

    Args:
        df (pd.DataFrame): DataFrame to analyze

    Returns:
        pd.DataFrame: DataFrame containing the statistics
    """
    return df.drop(columns=['Timestamp']).describe()
