from sqlalchemy import Column, Integer, Float
from app.db.base import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_item_order_id = Column(Integer, nullable=False)
    order_item_product_id = Column(Integer, nullable=False)
    order_item_quantity = Column(Integer, nullable=False)  # tinyint -> int
    order_item_subtotal = Column(Float, nullable=False)
    order_item_product_price = Column(Float, nullable=False)