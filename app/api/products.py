from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from starlette import status

from app.db.deps import get_db
from app.schemas.product import ProductList, ProductCreate
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])


''' API to get all suppliers'''
@router.get(path="/", response_model=List[ProductList])
def get_products(skip: int = Query(0, ge=0),limit: int = Query(10, le=100),db:Session = Depends(get_db)):
    return product_service.get_all_products(db, skip, limit)

@router.get(path="/{product_id}", response_model=ProductList)
def get_product(product_id:int, db:Session = Depends(get_db)):
    return product_service.get_product(product_id, db)

@router.post(
    "/",
    response_model=ProductList,
    status_code=status.HTTP_201_CREATED
)
def create_product(product: ProductCreate,db: Session = Depends(get_db)):
    try:
        return product_service.create_product(product.model_dump(), db)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to create product"
        )