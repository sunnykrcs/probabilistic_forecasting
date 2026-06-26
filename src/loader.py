import pandas as pd

from src.config import COLUMN_MAPPING

def load_csv(path):
    df = pd.read_csv(path)

    df = df.rename(columns=COLUMN_MAPPING)

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    return df