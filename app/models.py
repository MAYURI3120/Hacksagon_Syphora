from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from .database import Base
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))

    age = Column(Integer, nullable=True)
    weight = Column(Integer, nullable=True)
    gender = Column(String(10), nullable=True)
    height = Column(Integer, nullable=True)
    activity_level = Column(String(50), nullable=True)
    medical_conditions = Column(ARRAY(String), nullable=True)


class HydrationLog(Base):
    __tablename__ = "hydration_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    count = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
