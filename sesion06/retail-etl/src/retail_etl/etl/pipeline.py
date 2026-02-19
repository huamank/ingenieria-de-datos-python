import logging
from retail_etl.etl import extract, transform, load
from retail_etl.etl.state import get_watermark, set_watermark

log = logging.getLogger("retail_etl.pipeline")

def run_pipeline(settings, mysql_engine, mongo_db) -> None:
    meta_col = mongo_db[settings.col_meta]
    customers_col = mongo_db[settings.col_customers]
    products_col = mongo_db[settings.col_products]
    orders_col = mongo_db[settings.col_orders]

    # 1) Extract base
    log.info("Extracting base tables...")
    log.info("Extracting customers..")
    df_customers = extract.extract_customers(mysql_engine)
    log.info("Extracting departments..")
    df_depts = extract.extract_depts(mysql_engine)
    log.info("Extracting categories..")
    df_categories = extract.extract_categories(mysql_engine)
    log.info("Extracting products..")
    df_products = extract.extract_products(mysql_engine)

    # 2) Transform + Load base (full refresh by upsert)
    log.info("Transforming & loading customers/products...")
    log.info("Transforming & loading  customers..")
    cust_docs = transform.transform_customers(df_customers)
    log.info("Transforming & loading  products..")
    prod_docs = transform.transform_products(df_products, df_categories, df_depts)

    load.bulk_upsert(customers_col, cust_docs)
    load.bulk_upsert(products_col, prod_docs)

    # 3) Incremental Orders
    watermark = get_watermark(meta_col, settings.orders_watermark_key, settings.default_watermark)
    log.info("Orders watermark=%s", watermark)
    log.info("Extracting orders..")
    df_orders = extract.extract_orders_incremental(mysql_engine, watermark)
    order_ids = [int(x) for x in df_orders["order_id"].tolist()] if not df_orders.empty else []
    df_items = extract.extract_order_items_for_orders(mysql_engine, order_ids)
    log.info("Transforming & loading  orders..")
    order_docs, new_watermark = transform.transform_orders(df_orders, df_items, df_customers, df_products)

    if order_docs:
        log.info("Loading %s orders...", len(order_docs))
        load.bulk_upsert(orders_col, order_docs)

    if new_watermark:
        set_watermark(meta_col, settings.orders_watermark_key, new_watermark)
        log.info("Updated watermark=%s", new_watermark)

    # 4) Create indexes (idempotente)
    log.info("Ensuring indexes...")
    products_col.create_index([("category.id", 1)])
    products_col.create_index([("department.id", 1)])
    products_col.create_index([("name", 1)])
    orders_col.create_index([("customer.id", 1), ("order_date", -1)])
    orders_col.create_index([("status", 1)])