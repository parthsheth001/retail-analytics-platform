from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services import product_service

router = APIRouter(prefix="/products", tags=["Products"])


@router.get(path="/{product_id}")
def get_product(product_id:int, db:Session = Depends(get_db)):
    return product_service.get_product(product_id, db)