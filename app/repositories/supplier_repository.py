from app.models.supplier import Supplier

def get_all(db):
    return db.query(Supplier).all()


def get_by_id(supplier_id,db):
    return db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()