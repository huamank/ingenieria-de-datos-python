from pydantic import BaseModel, EmailStr

class CustomerOut(BaseModel):
    """
    Salida segura: NO expone customer_password
    """
    customer_id: int
    customer_fname: str
    customer_lname: str
    customer_email: str
    customer_street: str
    customer_city: str
    customer_state: str
    customer_zipcode: str

    model_config = {"from_attributes": True}