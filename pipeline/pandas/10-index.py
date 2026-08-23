#!/usr/bin/env python3
"""Sets the Timestamp column as the index of the DataFrame."""


def index(df):
    """Sets Timestamp as the index.

    Args:
        df (pd.DataFrame): DataFrame to modify

    Returns:
        pd.DataFrame: modified DataFrame
    """
    return df.set_index('Timestamp')
