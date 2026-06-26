import pandas as pd

def load_csv(path):
    """
    Load a CSV file with automatic date parsing.
    """
    df = pd.read_csv(path)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    elif "date_start" in df.columns:
        df["date"] = pd.to_datetime(df["date_start"])

    return df