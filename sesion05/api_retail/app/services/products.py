from sqlalchemy.orm import Session
from app.repositories import ProductsRepository

class ProductsService:
    def __init__(self, repo: ProductsRepository):
        self.repo = repo

    def list_products(
        self,
        db: Session,
        department_id: int | None,
        category_id: int | None,
        limit: int,
        offset: int,
    ):
        pass