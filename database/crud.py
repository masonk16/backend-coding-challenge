from sqlalchemy.orm import Session
import models
import schemas
#from . import models, schemas


def get_talent(db: Session, id: str):
    return db.query(models.Talent).filter(models.Talent.id == id).first()

def get_talents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Talent).offset(skip).limit(limit).all()

def create_talent(db: Session, talent: schemas.TalentCreate):
    db_talent = models.Talent(**vars(talent))
    db.add(db_talent)
    db.commit()
    db.refresh(db_talent)
    return db_talent

def get_manager(db: Session, id: str):
    return get_talent(db, id)


def get_managers(db: Session, skip: int = 0, limit: int = 100):
    return get_talents(db, skip, limit)


def create_manager(db: Session, manager: schemas.ManagerCreate):
    db_manager = models.Talent(**vars(manager))
    db.add(db_manager)
    db.commit()
    return db_manager

def get_client(db: Session, id: str):
    return db.query(models.Client).filter(models.Client.id == id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**vars(client))
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_skill(db: Session, name: str):
    return db.query(models.Skills).filter(models.Skills.name == name).first()

def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Skills).offset(skip).limit(limit).all()

def create_skill(db: Session, skills: schemas.SkillsCreate):
    db_skills = models.Skills(**vars(skills))
    db.add(db_skills)
    db.commit()
    db.refresh(db_skills)
    return db_skills

def get_plan_by_id(db: Session, id: int):
    return db.query(models.Planning).filter(models.Planning.id == id).first()

def get_plan_by_original_id(db: Session, original_id: int):
    return db.query(models.Planning).filter(models.Planning.original_id == original_id).first()

def get_plans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Planning).offset(skip).limit(limit).all()

def create_plan(db: Session, planning: schemas.PlanningCreate):
    db_planning = get_plan_by_id(db, id=planning.id)
    db_talent = get_talent(db, planning.talent_id)
    db_manager = get_talent(db, planning.manager_id)
    db_client = get_client(db, planning.client_id)
    db_required_skills = get_skill(db, planning.required_skills)
    db_optional_skills = get_skill(db, planning.optional_skills)

    planning_vars = vars(planning)
    del planning_vars["client_id"]
    planning_vars["client"] = db_client
    del planning_vars["manager_id"]
    planning_vars["manager"] = db_manager
    del planning_vars["talent_id"]
    planning_vars["talent"] = db_talent
    del planning_vars["required_skills"]
    planning_vars["required_skills"] = db_required_skills
    del planning_vars["optional_skills"]
    planning_vars["optional_skills"] = db_optional_skills

    db_planning = models.Planning(**planning_vars)

    db.add(db_planning)
    db.commit()
    db.refresh(db_planning)
    return db_planning
    