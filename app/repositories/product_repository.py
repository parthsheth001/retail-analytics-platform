from sqlalchemy.orm import Session

from app.models.product import Product


def get_all(db: Session, skip:int=0, limit:int=10):
    return db.query(Product).offset(skip).limit(limit).all()


def get_by_id(product_id, db):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()


def get_product_by_supplier_id(supplier_id: int, db):
    return db.query(Product).filter(
        Product.supplier_id == supplier_id
    ).all()


def create(product, db) -> Product:
    product = Product(**product)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
