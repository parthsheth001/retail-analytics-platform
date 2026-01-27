from fastapi import HTTPException

from app.repositories import supplier_repository, product_repository


def get_supplier(supplier_id, db):
    supplier = supplier_repository.get_by_id(supplier_id, db)
    if supplier:
        return supplier
    else:
        raise HTTPException(status_code=422, detail="Supplier not found")

def get_all_suppliers(db):
    suppliers = supplier_repository.get_all(db)
    return suppliers

def get_products_for_supplier(supplier_id: int, db):
    supplier = get_supplier(supplier_id, db)
    return product_repository.get_product_by_supplier_id(supplier_id, db)


def create_supplier(supplier,db):
    existing = supplier_repository.get_by_email(db, supplier.email)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Supplier already exists"
        )
    return supplier_repository.create(supplier,db)