import pandas as pd

def preprocess_data(df: pd.DataFrame):
    """Example preprocessing: fill NaN and ensure numeric types."""
    df = df.fillna(0)
    return df
