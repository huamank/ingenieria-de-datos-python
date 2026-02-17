from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    customer_fname = Column(String(45), nullable=False)
    customer_lname = Column(String(45), nullable=False)
    customer_email = Column(String(45), nullable=False)
    customer_password = Column(String(45), nullable=False)
    customer_street = Column(String(255), nullable=False)
    customer_city = Column(String(45), nullable=False)
    customer_state = Column(String(45), nullable=False)
    customer_zipcode = Column(String(45), nullable=False)