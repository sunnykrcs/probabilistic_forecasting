from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"

GOOGLE_FILE = DATA_DIR / "google_ads_campaign_stats.csv"
META_FILE = DATA_DIR / "meta_ads_campaign_stats.csv"
MS_FILE = DATA_DIR / "bing_campaign_stats.csv"

# GOOGLE_FILE = DATA_DIR / "google_ads.csv"
# META_FILE = DATA_DIR / "meta_ads.csv"
# MS_FILE = DATA_DIR / "microsoft_ads.csv"

OUTPUT_FILE = DATA_DIR / "master_dataset.csv"