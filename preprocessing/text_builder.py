import pandas as pd
from utils.config import PROCESSED_DATA_DIR

def build_documents():
    """
    Reads the processed SHL dataset and converts each row
    into a single rich text document.
    """
    csv_path = PROCESSED_DATA_DIR / "shl_assessments.csv"
    df = pd.read_csv(csv_path)

    documents = []

    for _, row in df.iterrows():
        text = f"""
        Assessment Name: {row['assessment_name']}
        Assessment Type: {row['assessment_type']}
        Skills Measured: {row['skills_measured']}
        Job Roles: {row['job_roles']}
        Description: {row['description']}
        Duration: {row['duration']} minutes
        """
        documents.append(text.strip())

    return documents


if __name__ == "__main__":
    docs = build_documents()
    print(f"✅ Built {len(docs)} documents")
    print("\nSample document:\n")
    print(docs[0])
