from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"

GOOGLE_FILE = DATA_DIR / "google_ads_campaign_stats.csv"
META_FILE = DATA_DIR / "meta_ads_campaign_stats.csv"
MS_FILE = DATA_DIR / "bing_campaign_stats.csv"

COLUMN_MAPPING = {
    "Campaign": "campaign_name",
    "campaign_name": "campaign_name",
    "CampaignName": "campaign_name",

    "Spend": "spend",
    "metrics_cost_micros": "spend",
    "spend": "spend",

    "date_start": "date",
    "TimePeriod": "date",
    "segments_date": "date"
}


OUTPUT_FILE = DATA_DIR / "master_dataset.csv"