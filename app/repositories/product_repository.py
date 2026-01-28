from sqlalchemy.orm import Session
from sqlalchemy import asc, desc
from app.models.product import Product


def get_all(
        db: Session,
        skip: int,
        limit: int,
        supplier_id=None,
        min_price=None,
        max_price=None,
        sort_by="id",
        order="asc"
):
    query = db.query(Product).filter(Product.is_active==True)

    if supplier_id is not None:
        query = query.filter(Product.supplier_id == supplier_id)

    if min_price is not None:
        query = query.filter(Product.price >= min_price)

    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    sort_column = getattr(Product, sort_by)
    query = query.order_by(asc(sort_column) if order == "asc" else desc(sort_column))

    return query.offset(skip).limit(limit).all()


def get_by_id(product_id, db):
    return db.query(Product).filter(Product.is_active==True,Product.id == product_id).first()


def get_product_by_supplier_id(supplier_id: int, db):
    return db.query(Product).filter(
        Product.supplier_id == supplier_id,Product.is_active==True
    ).all()


def create(product, db) -> Product:
    product = Product(**product)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def update(db_product, update_data, db) -> Product:
    for key, value in update_data.items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete(db_product, db) -> Product:
    db_product.is_active = False
    db.commit()
    db.refresh(db_product)
    return db_product