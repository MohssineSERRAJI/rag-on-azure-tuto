from config import Settings
from models import Passage
import pandas as pd

def main():

    df = pd.read_parquet("hf://datasets/enelpol/rag-mini-bioasq/text-corpus/test-00000-of-00001.parquet")
    df.rename(columns={"id": "_id"}, inplace=True)
    items = df.iloc[0:100, :].to_dict(orient='records')

    for item in items:
        try:
            passage = Passage(**item)
            passage.save()
            print(f"Ingested: {item}")
        except Exception as e:
            print(f"Error ingesting {item}: {e}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()

