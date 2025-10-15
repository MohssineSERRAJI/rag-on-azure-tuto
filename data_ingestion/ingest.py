from pymongo import MongoClient
from config import Settings

import pandas as pd


def main():
    settings = Settings()
    df = pd.read_parquet("hf://datasets/enelpol/rag-mini-bioasq/text-corpus/test-00000-of-00001.parquet")
    df.rename(columns={"id": "_id"}, inplace=True)
    items = df.iloc[0:100, :].to_dict(orient='records')
    
    client = MongoClient(settings.MONGODB_CONNECTION_STRING)
    db = client[settings.MONGODB_DATABASE]
    collection = db[settings.MONGODB_COLLECTION]

    for item in items:
        collection.replace_one({"_id": item["_id"]}, item, upsert=True)
        print(f"Ingested: {item}")

if __name__ == "__main__":
    main()
