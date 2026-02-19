from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_env: str
    mysql_uri: str
    mongo_uri: str
    mongo_db: str
    col_customers: str
    col_products: str
    col_orders: str
    col_meta: str
    orders_watermark_key: str
    default_watermark: str

def get_settings() -> Settings:
    return Settings(
        app_env=os.getenv("APP_ENV", "dev"),
        mysql_uri=os.environ["MYSQL_URI"],
        mongo_uri=os.environ["MONGO_URI"],
        mongo_db=os.getenv("MONGO_DB", "retail"),
        col_customers=os.getenv("MONGO_CUSTOMERS_COL", "customers"),
        col_products=os.getenv("MONGO_PRODUCTS_COL", "products"),
        col_orders=os.getenv("MONGO_ORDERS_COL", "orders"),
        col_meta=os.getenv("MONGO_META_COL", "etl_metadata"),
        orders_watermark_key=os.getenv("ORDERS_WATERMARK_KEY", "orders_etl"),
        default_watermark=os.getenv("DEFAULT_WATERMARK", "1970-01-01T00:00:00Z"),
    )