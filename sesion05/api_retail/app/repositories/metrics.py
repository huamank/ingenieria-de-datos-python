from sqlalchemy.orm import Session
from sqlalchemy import text

class MetricsRepository:
    def sales_by_department(self, db: Session, start: str, end: str) -> list[dict]:
       pass