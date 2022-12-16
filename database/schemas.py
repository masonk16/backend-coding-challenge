from datetime import datetime
from pydantic import BaseModel
from typing import Dict, List



class TalentBase(BaseModel):
    id: str
    name: str
    grade: str | None = None


class TalentCreate(TalentBase):
    pass


class Talent(TalentBase):
    class Config:
        orm_mode = True


class ManagerBase(BaseModel):
    id: str
    name: str


class Manager(ManagerBase):
    pass


class ManagerCreate(ManagerBase):
    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    id: str
    name: str
    industry: str


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    class Config:
        orm_mode = True


class SkillsBase(BaseModel):
    name: str
    category: str


class SkillsCreate(SkillsBase):
    pass


class Skills(SkillsBase):
    class Config:
        orm_mode = True


class PlanningBase(BaseModel):
    id: int
    original_id: str
    booking_grade: str | None = None
    operating_unit: str
    office_city: str
    office_postal_code: str
    total_hours: float
    start_date: str
    end_date: str


class PlanningCreate(PlanningBase):
    talent_id: str
    manager_id: str
    client_id: str
    required_skills: list[str]
    optional_skills: list[str]


class Planning(PlanningBase):
    talent: Talent | None = None
    manager: Manager
    client: Client
    required_skills: list[Skills] = []
    optional_skills: list[Skills] = []
    is_unassigned: bool

    class Config:
        orm_mode = True
