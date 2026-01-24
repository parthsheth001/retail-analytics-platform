from fastapi import FastAPI
from app.api.health import router as health_router
from app.db.base import Base
from app.db.session import engine
from app.api.suppliers import router as supplier_router
from app.api.products import router as product_router



app = FastAPI(title="Retail Analytics Platform")
Base.metadata.create_all(bind=engine)

'''Route for health check'''
app.include_router(health_router)

'''Route for suppliers'''
app.include_router(supplier_router)

'''Route for products'''
app.include_router(product_router)

@app.get('/')
def root():
    return {"status":"OK"}