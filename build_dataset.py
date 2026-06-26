from src.config import *

from src.loader import load_csv
from src.validator import validate
from src.cleaner import clean
from src.merger import prepare, merge
from src.aggregator import aggregate


def main():

    google = load_csv(GOOGLE_FILE)
    meta = load_csv(META_FILE)
    microsoft = load_csv(MS_FILE)

    validate(google, "Google")
    validate(meta, "Meta")
    validate(microsoft, "Microsoft")

    google = clean(google)
    meta = clean(meta)
    microsoft = clean(microsoft)

    google = prepare(google, "google")
    meta = prepare(meta, "meta")
    microsoft = prepare(microsoft, "microsoft")

    dataset = merge(
        google,
        meta,
        microsoft
    )

    dataset = aggregate(dataset)

    dataset.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(dataset.head())

    print("\nDataset shape:", dataset.shape)


if __name__ == "__main__":
    main()