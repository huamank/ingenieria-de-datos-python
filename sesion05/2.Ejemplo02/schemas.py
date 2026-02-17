from pydantic import BaseModel, EmailStr

class CustomerCreate(BaseModel):

    name: str
    email: EmailStr

class CustomerOut(BaseModel):
    
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True