from database import crud, models, schemas
import json
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine
from datetime import datetime

"""
Import json data to database
"""

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

with open("planning.json", "r") as planning_data:
    data = json.load(planning_data)
    for item in data:
        check_talent = (
            db.query(models.Talent).filter(models.Talent.id == item["talentId"]).first()
        )
        if check_talent is None:
            talent = crud.create_talent(
                db,
                schemas.TalentCreate(
                    **{
                        "id": item["talentId"],
                        "name": item["talentName"],
                        "grade": item["talentGrade"],
                    }
                ),
            )
        check_client = db.query(models.Client).filter(models.Client.id == item["clientId"]).first()
        if check_client is None:
            client = crud.create_client(
                db,
                schemas.ClientCreate(
                    **{
                        "id": item["clientId"],
                        "name": item["clientName"],
                        "industry": item["industry"],
                    }
                ),
            )
        check_manager = (
            db.query(models.Talent).filter(models.Talent.id == item["talentId"]).first()
        )
        if check_manager is None:
            manager = crud.create_manager(
                db,
                schemas.ManagerCreate(
                    **{"id": item["jobManagerId"], "name": item["jobManagerName"]}
                ),
            )
        check_start = (
            db.query(models.Planning)
            .filter(models.Planning.start_date == item["startDate"])
            .first()
        )
        if check_start is None:
            start_date = datetime.strptime(item["startDate"], "%m/%d/%Y %I:%M %p")
        check_end = (
            db.query(models.Planning)
            .filter(models.Planning.start_date == item["endDate"])
            .first()
        )
        if check_end is None:
            end_date = datetime.strptime(item["endDate"], "%m/%d/%Y %I:%M %p")
        check_planning = (
            db.query(models.Planning)
            .filter(models.Planning.original_id == item["originalId"])
            .first()
        )
        if check_planning is None:
            planning = crud.create_plan(
                db,
                schemas.PlanningCreate(
                    **{
                        "id": int(item["id"]),
                        "original_id": item["originalId"],
                        "booking_grade": item["bookingGrade"],
                        "operating_unit": item["operatingUnit"],
                        "office_city": item["officeCity"],
                        "office_postal_code": item["officePostalCode"],
                        "total_hours": float(item["totalHours"]),
                        "start_date": start_date,
                        "end_date": end_date,
                        "talent_id": talent.id,
                        "manager_id": manager.id,
                        "client_id": client.id,
                        "required_skills": required_skills,
                        "optional_skills": optional_skills,
                    }
                ),
            )
        required_skills = []
        for skill in item["requiredSkills"]:
            check_skills = (
                db.query(models.Skills).filter(models.Skills.name == skill).first()
            )
            if check_skills is None:
                required_skills.append(
                    crud.create_skill(db, schemas.SkillsCreate(**skill)).name
                )
        optional_skills = []
        for skill in item["optionalSkills"]:
            check_skills = (
                db.query(models.Skills).filter(models.Skills.name == skill).first()
            )
            if check_skills is None:
                optional_skills.append(
                    crud.create_skill(db, schemas.SkillsCreate(**skill)).name
                )
        # print("Importing record number:", planning.id)