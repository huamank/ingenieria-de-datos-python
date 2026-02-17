from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    order_date = Column(DateTime, nullable=False)
    order_customer_id = Column(Integer, nullable=False)
    order_status = Column(String(45), nullable=False)