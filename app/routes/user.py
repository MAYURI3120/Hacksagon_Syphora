from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, auth
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

# In-memory fallback DB (temporary)
fake_user_db = {}


# SIGNUP
@router.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = db.query(models.User).filter(models.User.email == user.email).first()
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

        hashed_password = auth.get_password_hash(user.password)
        new_user = models.User(
            name=user.username,
            email=user.email,
            password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except Exception as e:
        print(f"Database error during signup: {e}")
        # Fallback to fake DB
        if user.email in fake_user_db:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered (fallback)"
            )
        fake_user_db[user.email] = {
            "username": user.username,
            "password": user.password
        }
        return {
            "id": 0,
            "username": user.username,
            "email": user.email
        }


# LOGIN
@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = db.query(models.User).filter(models.User.email == user.email).first()
        if not db_user or not auth.pwd_context.verify(user.password, db_user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        return {"message": "Login successful"}

    except Exception as e:
        print(f"Database error during login: {e}")
        # Fallback login
        stored = fake_user_db.get(user.email)
        if not stored or stored["password"] != user.password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials (fallback)"
            )
        return {"message": "Login successful (fallback)"}
