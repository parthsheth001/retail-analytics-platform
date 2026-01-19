from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="Retail Analytics Platform")

'''Route for health check'''
app.include_router(health_router)

@app.get('/')
def root():
    return {"status":"OK"}