from fastapi import FastAPI
from app.config import settings
from app.routes import user, hydration
from app.database import Base, engine  # ✅ Fix: added missing imports

app = FastAPI()

# Include routers
app.include_router(user.router)
app.include_router(hydration.router)


@app.get("/")
def read_root():
    return {
        "message": "Backend is working!"
    }


# Optional: only runs when using `python main.py` directly (not uvicorn)
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
