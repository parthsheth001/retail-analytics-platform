from fastapi import HTTPException

from app.repositories import supplier_repository, product_repository


def get_products_for_supplier(supplier_id: int, db):
    supplier = supplier_repository.get_by_id(supplier_id, db)

    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")

    return product_repository.get_by_supplier_id(supplier_id, db)