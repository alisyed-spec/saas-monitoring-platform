from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Application
from ..schemas import AppCreate
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/apps")
def create_app(app: AppCreate, db: Session = Depends(get_db)):

    new_app = Application(
        name=app.name,
        owner_id=1,
        status="running"
    )

    db.add(new_app)
    db.commit()

    return {"message": "app created"}
