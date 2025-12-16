from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FAISS_DIR = BASE_DIR / "faiss_index"

def create_directories():
    for path in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, FAISS_DIR]:
        path.mkdir(parents=True, exist_ok=True)
