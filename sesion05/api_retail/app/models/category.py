from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    category_department_id = Column(Integer, nullable=False)
    category_name = Column(String(45), nullable=False)