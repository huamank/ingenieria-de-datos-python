from pydantic import BaseModel

class SalesByDepartmentRow(BaseModel):
    department_id: int
    department_name: str
    total_sales: float

class SalesByDepartmentResponse(BaseModel):
    start: str
    end: str
    data: list[SalesByDepartmentRow]