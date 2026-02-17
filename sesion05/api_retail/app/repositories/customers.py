from sqlalchemy.orm import Session
from app.models import Customer

class CustomersRepository:
    """
    Repositorio = capa de acceso a datos (queries ORM).
    """
    def list(self, db: Session, limit: int, offset: int) -> list[Customer]:
        return (
            db.query(Customer)
            .order_by(Customer.customer_id)
            .offset(offset)
            .limit(limit)
            .all()
        )

    def get(self, db: Session, customer_id: int) -> Customer | None:
        return db.query(Customer).filter(Customer.customer_id == customer_id).first()