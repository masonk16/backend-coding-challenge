from sqlalchemy.orm import Session

from . import models, schemas


def get_plan_by_id(db: Session, id: int):
    return db.query(models.Planning).filter(models.Planning.id == id).first()

def get_plan_by_original_id(db: Session, original_id: int):
    return db.query(models.Planning).filter(models.Planning.original_id == original_id).first()

def get_plans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Planning).offset(skip).limit(limit).all()

def get_talent(db: Session, id: str):
    return db.query(models.Talent).filter(models.Talent.id == id).first()

def get_talents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Talent).offset(skip).limit(limit).all()

def get_client(db: Session, id: str):
    return db.query(models.Client).filter(models.Client.id == id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def get_skill(db: Session, name: str):
    return db.query(models.Skills).filter(models.Skills.name == name).first()

def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skills).offset(skip).limit(limit).all()

