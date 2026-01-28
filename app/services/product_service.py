from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import product_repository
from app.services import supplier_service

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
    if product["price"] < 0:
        raise HTTPException(status_code=422, detail="Price cannot be negative value.")
    supplier_service.get_supplier(product["supplier_id"],db)
    return product_repository.create(product, db)

def update_product(product_id, product, db):
    db_product = get_product(product_id, db) #checks if product exists
    update_data = product.dict(exclude_unset=True)

    # --- Business validations ---
    if "price" in update_data and update_data["price"] <= 0:
        raise HTTPException(status_code=422, detail="Price must be greater than zero.")

    if "name" in update_data and not update_data["name"]:
        raise HTTPException(status_code=422, detail="Name cannot be empty.")

    if "supplier_id" in update_data:
        supplier_service.get_supplier(update_data["supplier_id"], db)

    return product_repository.update(db_product, update_data, db)

    # if "price" in product and (product["price"] < 0 or product["price"] is None):
    #     raise HTTPException(status_code=422, detail="Price cannot be negative value.")
    #
    # if "name" in product and product["name"] is None:
    #     raise HTTPException(status_code=422, detail="Name cannot be empty.")
    #
    # if "supplier_id" in product and product["supplier_id"] is None:
    #     raise HTTPException(status_code=422, detail="Supplier_id cannot be empty.")
    #
    # supplier_service.get_supplier(product["supplier_id"],db)
    #
    # return product_repository.update(db_product,product, db)

def delete_product(product_id, db):
    db_product = get_product(product_id, db) #checks if product exists
    deleted = product_repository.delete(db_product, db)
    return True if deleted else False