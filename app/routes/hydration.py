from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models, schemas
from ..auth import get_current_user

router = APIRouter(prefix="/hydration", tags=["Hydration"])


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/log", response_model=schemas.HydrationLogOut)
def log_hydration(
    hydration: schemas.HydrationLogCreate,
    db: Session = Depends(get_db),
    user: models.User = Depends(get_current_user)
):
    new_log = models.HydrationLog(
        user_id=user.id,
        count=hydration.count
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log
