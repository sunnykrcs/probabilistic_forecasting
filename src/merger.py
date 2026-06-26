import pandas as pd

CHANNEL_MAP = {
    "google": "Google Ads",
    "meta": "Meta Ads",
    "microsoft": "Microsoft Ads"
}


def prepare(df, channel):

    df = df.copy()

    df["channel"] = CHANNEL_MAP[channel]

    if "revenue" not in df.columns:

        if "conversion" in df.columns:
            df["revenue"] = df["conversion"]

        else:
            df["revenue"] = 0

    df["roas"] = df["revenue"] / df["spend"].replace(0, 1)

    return df


def merge(google, meta, microsoft):

    return pd.concat(
        [
            google,
            meta,
            microsoft
        ],
        ignore_index=True
    )