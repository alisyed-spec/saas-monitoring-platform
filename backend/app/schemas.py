from pydantic import BaseModel


class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class AppCreate(BaseModel):
    name: str


class MetricCreate(BaseModel):
    app_id: int
    cpu_usage: float
    memory_usage: float
    response_time: float


class AlertCreate(BaseModel):
    app_id: int
    message: str
    severity: str
