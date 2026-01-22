from app.models.product import Product


def get_by_supplier_id(supplier_id: int,db):
    return db.query(Product).filter(
        Product.supplier_id == supplier_id
    ).all()