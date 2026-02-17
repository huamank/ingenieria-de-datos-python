from pydantic import BaseModel, Field

class Pagination(BaseModel):
    limit: int = Field(50, ge=1, le=200)
    offset: int = Field(0, ge=0)