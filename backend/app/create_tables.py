from app.database import engine, Base
import app.models.user

Base.metadata.create_all(bind=engine)
