import pandas as pd
from sqlalchemy.engine import Engine
from sqlalchemy import text, bindparam
def extract_customers(engine: Engine) -> pd.DataFrame:
    q = """
    SELECT customer_id, customer_fname, customer_lname, customer_email,
           customer_street, customer_city, customer_state, customer_zipcode
    FROM customers
    """
    return pd.read_sql_query(q, engine)

def extract_depts(engine: Engine) -> pd.DataFrame:
    return pd.read_sql_query("SELECT department_id, department_name FROM departments", engine)

def extract_categories(engine: Engine) -> pd.DataFrame:
    q = "SELECT category_id, category_department_id, category_name FROM categories"
    return pd.read_sql_query(q, engine)

def extract_products(engine: Engine) -> pd.DataFrame:
    q = """
    SELECT product_id, product_category_id, product_name, product_description,
           product_price, product_image
    FROM products
    """
    return pd.read_sql_query(q, engine)

def extract_orders_incremental(engine: Engine, watermark_iso: str) -> pd.DataFrame:
    q = """
    SELECT order_id, order_date, order_customer_id, order_status
    FROM orders
    WHERE order_date > %(watermark)s
    """
    return pd.read_sql_query(q, engine, params={"watermark": watermark_iso})

def extract_order_items_for_orders(engine: Engine, order_ids: list[int]) -> pd.DataFrame:
    if not order_ids:
        return pd.DataFrame(columns=[
            "order_item_id","order_item_order_id","order_item_product_id",
            "order_item_quantity","order_item_subtotal","order_item_product_price"
        ])
    
    stmt = text("""
        SELECT order_item_id, order_item_order_id, order_item_product_id,
               order_item_quantity, order_item_subtotal, order_item_product_price
        FROM order_items
        WHERE order_item_order_id IN :order_ids
    """).bindparams(bindparam("order_ids", expanding=True))

    return pd.read_sql_query(stmt, engine, params={"order_ids": order_ids})