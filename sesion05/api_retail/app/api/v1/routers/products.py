from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import ProductOut
from app.repositories import ProductsRepository
from app.services import ProductsService

router = APIRouter(prefix="/products", tags=["products"])

service = ProductsService(ProductsRepository())

@router.get("", response_model=list[ProductOut])
def list_products(
    department_id: int | None = Query(None),
    category_id: int | None = Query(None),
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    pass