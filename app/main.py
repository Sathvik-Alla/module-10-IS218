from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import Base, engine, get_db
from app.models import User
from app.schemas import UserCreate, UserRead
from app.security import hash_password

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Module 10 - Secure User Model")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/users", response_model=UserRead, status_code=201)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hash_password(user_in.password),
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Username or email already exists")
    db.refresh(user)
    return user