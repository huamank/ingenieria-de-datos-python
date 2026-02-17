from pydantic import BaseModel
from datetime import datetime

class OrderOut(BaseModel):
    order_id: int
    order_date: datetime
    order_customer_id: int
    order_status: str

    model_config = {"from_attributes": True}

class OrderItemOut(BaseModel):
    order_item_id: int
    order_item_order_id: int
    order_item_product_id: int
    order_item_quantity: int
    order_item_subtotal: float
    order_item_product_price: float

    model_config = {"from_attributes": True}

class OrderWithItems(BaseModel):
    order: OrderOut
    items: list[OrderItemOut]