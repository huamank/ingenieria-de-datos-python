from typing import Optional
from pymongo.collection import Collection
from datetime import datetime, timezone

def get_watermark(meta_col: Collection, key: str, default_iso: str) -> str:
    doc = meta_col.find_one({"_id": key})
    return (doc or {}).get("watermark", default_iso)

def set_watermark(meta_col: Collection, key: str, watermark_iso: str) -> None:
    meta_col.update_one(
        {"_id": key},
        {"$set": {"watermark": watermark_iso, "updated_at": datetime.now(timezone.utc)}},
        upsert=True
    )