from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Alert
from ..schemas import AlertCreate
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/alerts")
def create_alert(alert: AlertCreate, db: Session = Depends(get_db)):

    new_alert = Alert(**alert.dict())

    db.add(new_alert)
    db.commit()

    return {"message": "alert created"}
