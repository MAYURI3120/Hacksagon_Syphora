# backend/app/main.py
from fastapi import FastAPI
from app.config import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello FastAPI",
        "database_url": settings.DATABASE_URL,  # using imported setting
        "env_secret_key": settings.SECRET_KEY
    }
def read_root():
    return {"message": "Backend is working!"}
