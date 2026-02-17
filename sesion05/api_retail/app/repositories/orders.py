from sqlalchemy.orm import Session
from app.models import Order, OrderItem

class OrdersRepository:
    def get_order(self, db: Session, order_id: int) -> Order | None:
        return db.query(Order).filter(Order.customer_id == order_id).first()
    
    def list_items(self, db: Session, order_id: int) -> list[OrderItem]:
        return (
            db.query(OrderItem)
            .filter(OrderItem.order_item_order_id == order_id)
            .all()
        )