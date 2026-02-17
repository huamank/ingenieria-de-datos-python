from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import CustomersRepository

class CustomersService:
    """
    Service = lógica de negocio (validaciones, reglas).
    """
    def __init__(self, repo: CustomersRepository):
        self.repo = repo

    def list_customers(self, db: Session, limit: int, offset: int):
        return self.repo.list(db, limit, offset)

    def get_customer(self, db: Session, customer_id: int):
        customer = self.repo.get(db, customer_id)
        return customer