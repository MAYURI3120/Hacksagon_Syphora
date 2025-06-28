from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# No SQLite-specific config, this works for postgreSQL:
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# to use in FastAPI dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
