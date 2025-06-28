from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, hydration, chatbot  #  make sure this resolves

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(user.router)
app.include_router(hydration.router)
app.include_router(chatbot.router)


@app.get("/")
def read_root():
    return {"message": "Backend is working!"}
