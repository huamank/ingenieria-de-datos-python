from sqlalchemy.orm import Session
from app.repositories import MetricsRepository

class MetricsService:
    def __init__(self, repo: MetricsRepository):
        self.repo = repo

    def sales_by_department(self, db: Session, start: str, end: str):
        pass