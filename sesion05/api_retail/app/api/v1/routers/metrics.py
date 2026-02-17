from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas import SalesByDepartmentResponse
from app.repositories import MetricsRepository
from app.services import MetricsService

router = APIRouter(prefix="/metrics", tags=["metrics"])

service = MetricsService(MetricsRepository())

@router.get("/sales_by_department", response_model=SalesByDepartmentResponse)
def sales_by_department(
    start: str = Query(..., description="YYYY-MM-DD"),
    end: str = Query(..., description="YYYY-MM-DD"),
    db: Session = Depends(get_db),
):
    pass