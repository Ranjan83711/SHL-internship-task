import json
import pandas as pd
from utils.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, create_directories

def clean_data():
    create_directories()

    with open(RAW_DATA_DIR / "shl_raw_scraped.json", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["assessment_name", "description"], inplace=True)

    output = PROCESSED_DATA_DIR / "shl_assessments.csv"
    df.to_csv(output, index=False)

    print("Cleaned data saved to", output)

if __name__ == "__main__":
    clean_data()
