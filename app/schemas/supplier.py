from pydantic import BaseModel

class SupplierBase(BaseModel):
    name: str
    email: str

class SupplierCreate(SupplierBase):
    pass

class SupplierResponse(SupplierBase):
    id: int

    class Config:
        from_attributes = True
