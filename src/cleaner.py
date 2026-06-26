import numpy as np

def clean(df):

    df = df.copy()

    numeric = [
        "spend",
        "clicks",
        "impressions",
        "conversion",
        "revenue",
        "ctr",
        "cpc",
        "cpm"
    ]

    for col in numeric:

        if col in df.columns:
            df[col] = (
                df[col]
                .fillna(0)
                .astype(float)
            )

    df["campaign_name"] = (
        df["campaign_name"]
        .fillna("Unknown")
    )

    return df