from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your frontend (React app on port 5173)
origins = [
    "http://localhost:5173",   # ✅ React dev server
    "http://127.0.0.1:5173",   # ✅ Alternate localhost
    "*"                        # ⚠️ Allows all (not recommended in production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # 👈 Frontend URLs allowed
    allow_credentials=True,
    allow_methods=["*"],               # 👈 Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],               # 👈 Allow all headers (e.g., Authorization)
)
