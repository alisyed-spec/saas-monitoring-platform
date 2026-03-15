from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Application
from ..schemas import AppCreate
from ..database import SessionLocal
from ..security import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/apps")
def create_app(
    app: AppCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    new_app = Application(
        name=app.name,
        owner_id=user_id,
        status="running"
    )

    db.add(new_app)
    db.commit()

    return {"message": "app created"}
