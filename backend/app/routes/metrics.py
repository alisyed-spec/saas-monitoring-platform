from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import Metric
from ..schemas import MetricCreate
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/metrics")
def send_metrics(metric: MetricCreate, db: Session = Depends(get_db)):

    new_metric = Metric(**metric.dict())

    db.add(new_metric)
    db.commit()

    return {"message": "metric stored"}
