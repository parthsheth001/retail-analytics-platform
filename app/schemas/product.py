from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(BaseModel):
    name: str
    price: float # = Field(gt=0)
    supplier_id: int

class ProductList(BaseModel):
    id: int
    name: str
    price: float
    supplier_id: int

    class Config:
        from_attributes = True