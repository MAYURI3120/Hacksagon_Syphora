from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: Optional[int] = None
    weight: Optional[int] = None
    gender: Optional[str] = None
    height: Optional[int] = None
    activity_level: Optional[str] = None
    medical_conditions: Optional[List[str]] = None


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: Optional[int]
    weight: Optional[int]
    gender: Optional[str]
    height: Optional[int]
    activity_level: Optional[str]
    medical_conditions: Optional[List[str]]

    class Config:
        from_attributes = True


# ✅ Move these outside UserOut
class HydrationLogCreate(BaseModel):
    count: int


class HydrationLogOut(BaseModel):
    id: int
    user_id: int
    count: int
    amount_ml: float
    timestamp: datetime

    class Config:
        from_attributes = True
