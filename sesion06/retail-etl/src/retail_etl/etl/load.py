from pymongo.collection import Collection
from pymongo import UpdateOne

def bulk_upsert(col: Collection, docs: list[dict], batch_size: int = 1000) -> int:
    if not docs:
        return 0

    total = 0
    for i in range(0, len(docs), batch_size):
        batch = docs[i:i+batch_size]
        ops = [
            UpdateOne({"_id": d["_id"]}, {"$set": d}, upsert=True)
            for d in batch
        ]
        res = col.bulk_write(ops, ordered=False)
        total += (res.upserted_count + res.modified_count + res.matched_count)
    return total