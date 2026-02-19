from __future__ import annotations
import pandas as pd
from datetime import datetime, timezone

def _utc_now():
    return datetime.now(timezone.utc)

def transform_customers(df: pd.DataFrame) -> list[dict]:
    now = _utc_now()
    df = df.copy()
    df["customer_email"] = df["customer_email"].str.strip().str.lower()

    docs = []
    for r in df.itertuples(index=False):
        docs.append({
            "_id": int(r.customer_id),
            "first_name": r.customer_fname,
            "last_name": r.customer_lname,
            "email": r.customer_email,
            "address": {
                "street": r.customer_street,
                "city": r.customer_city,
                "state": r.customer_state,
                "zipcode": r.customer_zipcode,
            },
            "updated_at": now
        })
    return docs

def transform_products(df_products: pd.DataFrame,
                       df_categories: pd.DataFrame,
                       df_depts: pd.DataFrame) -> list[dict]:
    now = _utc_now()
    # enrich: products -> categories -> departments
    df = df_products.merge(
        df_categories,
        left_on="product_category_id",
        right_on="category_id",
        how="left"
    ).merge(
        df_depts,
        left_on="category_department_id",
        right_on="department_id",
        how="left"
    )

    docs = []
    for r in df.itertuples(index=False):
        docs.append({
            "_id": int(r.product_id),
            "name": r.product_name,
            "description": r.product_description,
            "price": float(r.product_price),
            "image": r.product_image,
            "category": {"id": int(r.category_id) if pd.notna(r.category_id) else None,
                         "name": r.category_name},
            "department": {"id": int(r.department_id) if pd.notna(r.department_id) else None,
                           "name": r.department_name},
            "updated_at": now
        })
    return docs

def transform_orders(df_orders: pd.DataFrame,
                     df_items: pd.DataFrame,
                     df_customers: pd.DataFrame,
                     df_products: pd.DataFrame) -> tuple[list[dict], str]:
    """
    Retorna:
      - docs orders list
      - new watermark ISO (max order_date)
    """
    if df_orders.empty:
        return [], ""

    now = _utc_now()

    # customers lookup (mínimo para order doc)
    cust_min = df_customers[["customer_id","customer_fname","customer_lname","customer_email"]].copy()
    cust_min["customer_email"] = cust_min["customer_email"].str.strip().str.lower()

    # products lookup mínimo
    prod_min = df_products[["product_id","product_name","product_category_id"]].copy()

    # items enrich: order_items -> products
    items = df_items.merge(
        prod_min,
        left_on="order_item_product_id",
        right_on="product_id",
        how="left"
    )

    # orders enrich: orders -> customers
    orders = df_orders.merge(
        cust_min,
        left_on="order_customer_id",
        right_on="customer_id",
        how="left"
    )

    # agrupar items por order_id
    items_grouped = {}
    for r in items.itertuples(index=False):
        oid = int(r.order_item_order_id)
        items_grouped.setdefault(oid, []).append({
            "order_item_id": int(r.order_item_id),
            "product": {
                "id": int(r.order_item_product_id),
                "name": r.product_name,
                "category_id": int(r.product_category_id) if pd.notna(r.product_category_id) else None
            },
            "quantity": int(r.order_item_quantity),
            "product_price": float(r.order_item_product_price),
            "subtotal": float(r.order_item_subtotal),
        })

    docs = []
    for r in orders.itertuples(index=False):
        oid = int(r.order_id)
        its = items_grouped.get(oid, [])
        total = sum(i["subtotal"] for i in its)
        docs.append({
            "_id": oid,
            "order_date": r.order_date.to_pydatetime().replace(tzinfo=timezone.utc)
                if hasattr(r.order_date, "to_pydatetime") else r.order_date,
            "status": r.order_status,
            "customer": {
                "id": int(r.order_customer_id),
                "first_name": r.customer_fname,
                "last_name": r.customer_lname,
                "email": r.customer_email,
            },
            "items": its,
            "metrics": {"items_count": len(its), "total_amount": float(total)},
            "updated_at": now
        })

    # nuevo watermark = max(order_date)
    max_dt = pd.to_datetime(df_orders["order_date"]).max()
    new_watermark = max_dt.to_pydatetime().replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
    return docs, new_watermark