from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import CustomerOut
from app.repositories import CustomersRepository
from app.services import CustomersService

router = APIRouter(prefix="/customers", tags=["customers"])

service = CustomersService(CustomersRepository())

@router.get("", response_model=list[CustomerOut])
def list_customers(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return service.list_customers(db, limit, offset)

@router.get("/{customer_id}", response_model=CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return service.get_customer(db, customer_id)