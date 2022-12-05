from fastapi import Depends, FastAPI, HTTPException
from fastapi_pagination import Page, paginate, add_pagination
from sqlalchemy.orm import Session
from . import crud
from . import models
from . import schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

add_pagination(app)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/talent/{id}", response_model=schemas.Talent)
def read_talent(id: str, db: Session = Depends(get_db)):
    db_talent = crud.get_talent(db, id=id)
    if db_talent is None:
        raise HTTPException(status_code=404, detail="Talent not found")
    return db_talent


@app.get("/talent/", response_model=list[schemas.Talent])
def read_talents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    talents = crud.get_talents(db, skip=skip, limit=limit)
    return talents


@app.get("/client/{id}", response_model=schemas.Client)
def read_client(id: str, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, id=id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client


@app.get("/client/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients


@app.get("/skills/", response_model=schemas.Skills)
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    skills = crud.get_skills(db, skip=skip, limit=limit)
    return skills


@app.get("/planning/", response_model=Page[list[schemas.Planning]])
def read_planning(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    planning = crud.get_plans(db, skip=skip, limit=limit)
    return paginate(planning)


@app.get("/planning/{id}", response_model=schemas.Planning)
def read_planning(id: int, db: Session = Depends(get_db)):
    db_planning = crud.get_plan_by_id(db, id=id)
    if db_planning is None:
        raise HTTPException(status_code=404, detail="Plan not found")
    return db_planning


@app.get("/planning/{original_id}", response_model=schemas.Planning)
def read_planning(original_id: str, db: Session = Depends(get_db)):
    db_planning = crud.get_plan_by_original_id(db, original_id=original_id)
    if db_planning is None:
        raise HTTPException(status_code=404, detail="Plan not found")
    return db_planning
