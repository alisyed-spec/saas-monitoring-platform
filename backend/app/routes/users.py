from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User
from ..schemas import UserCreate
from ..auth import hash_password
from ..schemas import UserLogin

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed = hash_password(user.password)

    new_user = User(
        email=user.email,
        password_hash=hashed
    )

    db.add(new_user)
    db.commit()

    return {"message": "user created"}
router = APIRouter()

# existing endpoint
@router.post("/users")
def create_user():
    ...

# NEW login endpoint
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="invalid credentials")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="invalid credentials")

    token = create_access_token({"user_id": db_user.id})

    return {"access_token": token}
