import pandas as pd

def aggregate(df):

    grouped = (

        df.groupby(
            [
                "date",
                "channel",
                "campaign_name"
            ],
            as_index=False
        )

        .agg(
            spend=("spend", "sum"),
            revenue=("revenue", "sum"),
            clicks=("clicks", "sum"),
            impressions=("impressions", "sum"),
            conversions=("conversion", "sum")
        )

    )

    grouped["roas"] = (
        grouped["revenue"] /
        grouped["spend"].replace(0, 1)
    )

    return grouped