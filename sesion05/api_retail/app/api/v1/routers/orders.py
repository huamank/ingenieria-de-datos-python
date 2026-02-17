from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import OrderWithItems
from app.repositories import OrdersRepository
from app.services import OrdersService

router = APIRouter(prefix="/orders", tags=["orders"])

service = OrdersService(OrdersRepository())

@router.get("/{order_id}", response_model=OrderWithItems)
def get_order(order_id: int, db: Session = Depends(get_db)):
    pass