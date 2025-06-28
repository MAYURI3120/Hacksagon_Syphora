from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from .database import Base


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
