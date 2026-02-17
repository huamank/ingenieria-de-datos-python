from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_category_id = Column(Integer, nullable=False)
    product_name = Column(String(45), nullable=False)
    product_description = Column(String(255), nullable=False)
    product_price = Column(Float, nullable=False)
    product_image = Column(String(255), nullable=False)