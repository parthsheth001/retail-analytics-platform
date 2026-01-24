from pydantic import BaseModel, EmailStr


class SupplierBase(BaseModel):
    name: str
    email: EmailStr

class SupplierCreate(SupplierBase):
    pass

class SupplierList(SupplierBase):
    id: int

    class Config:
        from_attributes = True
