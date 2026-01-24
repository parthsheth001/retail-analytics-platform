from app.models.supplier import Supplier

def get_all(db):
    return db.query(Supplier).all()


def get_by_id(supplier_id,db):
    return db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()

def get_by_email(db, email):
    return db.query(Supplier).filter(
        Supplier.email == email
    ).first()

def create(supplier,db):
    db_supplier = Supplier(**supplier)
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier