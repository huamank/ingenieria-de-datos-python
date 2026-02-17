from sqlalchemy.orm import Session
from sqlalchemy import text
from app.models import Product

class ProductsRepository:
    def list_all(self, db: Session, limit: int, offset: int) -> list[Product]:
        pass

    def list_by_category(self, db: Session, category_id: int, limit: int, offset: int) -> list[Product]:
        pass

    def list_by_department(self, db: Session, department_id: int, limit: int, offset: int) -> list[Product]:
        pass