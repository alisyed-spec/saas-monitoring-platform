from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes import users, apps, metrics, alerts

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Monitoring Platform")

app.include_router(users.router)
app.include_router(apps.router)
app.include_router(metrics.router)
app.include_router(alerts.router)

@app.get("/")
def root():
	return {"message": "API running"}
