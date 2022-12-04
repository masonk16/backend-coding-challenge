from datetime import datetime
from pydantic import BaseModel


class TalentBase(BaseModel):
    id: str
    name: str
    talent_grade: str | None = None
    booking_grade: str | None = None
    operating_unit: str
    office_city: str
    office_postal_code: str 

class Talent(TalentBase):
    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    id: str
    name: str
    industry: str

class Client(ClientBase):
    class Config:
        orm_mode = True

class SkillBase(BaseModel):
    name: str
    category: str

class Skill(SkillBase):
    class Config:
        orm_mode = True

class PlanningBase(BaseModel):
    id: int
    original_id: str
    total_hours: float
    start_date: datetime
    end_date: datetime

class Planning(PlanningBase):
    talent: Talent | None = None
    manager: Talent
    client: Client
    required_skills: list[Skill] = []
    optional_skills: list[Skill] = []
    is_unassigned: bool
    class Config:
        orm_mode = True