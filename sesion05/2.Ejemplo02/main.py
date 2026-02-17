from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from db import Base, engine, SessionLocal
from models import Customer
from schemas import CustomerCreate, CustomerOut


Base.metadata.create_all(bind=engine)

app = FastAPI(title="API con DB")

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# crear cliente

@app.post("/customers", response_model=CustomerOut, status_code=201)
def create_customer(payload: CustomerCreate, db: Session = Depends(get_db)):
    
    exists = db.query(Customer).filter(Customer.email == payload.email).first()
    print(exists)
    if exists:
         raise HTTPException(status_code=409, detail = "Email ya existe")
    
    customer = Customer(name=payload.name, email=payload.email)

    db.add(customer)
    db.commit()
    db.refresh(customer) # podemos obtener el id generado

    return customer

# listar clientes

@app.get("/customers", response_model=list[CustomerOut])
def list_customers(db: Session = Depends(get_db)):
    return db.query(Customer).order_by(Customer.id).all()