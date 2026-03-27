from fastapi import FastAPI, Request
import time
from prometheus_fastapi_instrumentator import Instrumentator
from app.database import engine, Base
from app import models
from app.routes import users, apps, metrics, alerts
from .logger import logger

app = FastAPI(title="SaaS Monitoring Platform")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(f"{request.method} {request.url.path} completed in {process_time:.4f}s")

    return response


Base.metadata.create_all(bind=engine)

Instrumentator().instrument(app).expose(app)

logger.info("API service started")

app.include_router(users.router)
app.include_router(apps.router)
app.include_router(metrics.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
