from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.supplier import SupplierCreate, SupplierResponse
from app.db.models import Supplier

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.post("/", response_model=SupplierResponse)
def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    db_supplier = Supplier(
        name=supplier.name,
        email=supplier.email
    )
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier
