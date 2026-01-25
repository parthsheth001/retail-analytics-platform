from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import product_repository

ALLOWED_SORT_FIELDS = {"id", "price", "name"}
ALLOWED_ORDER = {"asc", "desc"}

def get_product(product_id, db):
    product = product_repository.get_by_id(product_id, db)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

def get_all_products(
        db: Session,
        skip: int,
        limit: int,
        supplier_id: int | None,
        min_price: float | None,
        max_price: float | None,
        sort_by: str,
        order: str
):
    if sort_by not in ALLOWED_SORT_FIELDS:
        raise ValueError("Invalid sort field")

    if order not in ALLOWED_ORDER:
        raise ValueError("Invalid order")

    return product_repository.get_all(
        db=db,
        skip=skip,
        limit=limit,
        supplier_id=supplier_id,
        min_price=min_price,
        max_price=max_price,
        sort_by=sort_by,
        order=order
    )

def create_product(product, db):
    return product_repository.create(product, db)