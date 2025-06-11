from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import engine, SessionLocal, Base

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="MY WORKOUT API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/workouts/", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    db_workout = models.Workout(**workout.dict())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

@app.get("/workouts/", response_model=list[schemas.Workout])
def read_workouts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Workout).offset(skip).limit(limit).all()
