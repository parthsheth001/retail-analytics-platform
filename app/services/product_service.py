from fastapi import HTTPException
from app.repositories import product_repository


def get_product(product_id, db):
    product = product_repository.get_by_id(product_id, db)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")

def get_all_products(db, skip: int,limit: int):
    return product_repository.get_all(db,  skip, limit)

def create_product(product, db):
    return product_repository.create(product, db)