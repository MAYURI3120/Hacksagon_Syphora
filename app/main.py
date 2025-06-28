# app/main.py
from fastapi import FastAPI
from app.routes import user
from app.database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)


@app.get("/")
def read_root():
    return {"message": "API working fine"}
