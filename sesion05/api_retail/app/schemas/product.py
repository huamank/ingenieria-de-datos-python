from pydantic import BaseModel

class ProductOut(BaseModel):
    product_id: int
    product_category_id: int
    product_name: str
    product_description: str
    product_price: float
    product_image: str

    model_config = {"from_attributes": True}