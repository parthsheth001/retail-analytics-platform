from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.supplier import SupplierCreate, SupplierResponse
from app.models.supplier import Supplier
from app.services import supplier_service

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


@router.get(path="/")
def get_suppliers(db:Session = Depends(get_db)):
    all_suppliers = db.query(Supplier).all()
    return all_suppliers


@router.get(path="/{supplier_id}")
def get_suppliers(supplier_id:int, db:Session = Depends(get_db)):
    supplier = db.get(Supplier,supplier_id)
    if supplier:
        return supplier
    else:
        raise HTTPException(status_code=404, detail="Supplier not found")

@router.get(path="/{supplier_id}/products")
def get_products(supplier_id:int, db:Session = Depends(get_db)):
    return supplier_service.get_products_for_supplier(supplier_id, db)