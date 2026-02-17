from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import OrdersRepository

class OrdersService:
    def __init__(self, repo: OrdersRepository):
        self.repo = repo

    def get_order_with_items(self, db: Session, order_id: int):
        order = self.repo.get_order(db, order_id)
        items = self.repo.list_items(db, order_id)

        return { "Order": order, "items": items}