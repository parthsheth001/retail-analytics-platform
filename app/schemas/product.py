from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    pass

class ProductCreate(BaseModel):
    name: str
    price: float
    supplier_id: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    supplier_id: Optional[int] = None

class ProductList(BaseModel):
    id: int
    name: str
    price: float
    supplier_id: int

    class Config:
        from_attributes = True