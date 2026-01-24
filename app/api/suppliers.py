from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.schemas.product import ProductList, ProductCreate
from app.schemas.supplier import SupplierCreate, SupplierList
from app.services import supplier_service, product_service

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

''' API to get all suppliers'''
@router.get(path="/", response_model=List[SupplierList])
def get_suppliers(db:Session = Depends(get_db)):
    return supplier_service.get_all_suppliers(db)

''' API to get a specific/single supplier based on Supplier ID'''
@router.get(path="/{supplier_id}", response_model=SupplierList)
def get_supplier(supplier_id:int, db:Session = Depends(get_db)):
    return supplier_service.get_supplier(supplier_id, db)

''' API to get all products for a specific/single supplier based on Supplier ID'''
@router.get(path="/{supplier_id}/products", response_model=List[ProductList])
def get_products(supplier_id:int, db:Session = Depends(get_db)):
    return supplier_service.get_products_for_supplier(supplier_id, db)

''' API to create supplier'''
@router.post("/", response_model=SupplierList)
def create_supplier(supplier: SupplierCreate,db: Session = Depends(get_db)):
    return supplier_service.create_supplier(supplier.model_dump(),db)


# ''' API to create products for a specific/single supplier based on Supplier ID'''
# @router.post(path="/{supplier_id}/products", response_model=ProductResponse)
# def create_product(supplier_id:int, product:ProductCreate, db:Session = Depends(get_db)):
#     try:
#         product = product_service.create_product_for_supplier(supplier_id, product, db)
#         return product
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))
