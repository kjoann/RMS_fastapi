from fastapi import FastAPI
from app.routers import retail
from app.database import engine
from app.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(retail.router)

@app.get("/")
def root():
    return {"message": "Welcome to my Retail Management System!"}